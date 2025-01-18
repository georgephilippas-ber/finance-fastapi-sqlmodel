# pip install --upgrade --quiet  llama-cpp-python
# https://model.lmstudio.ai/download/lmstudio-community/granite-3.1-8b-instruct-GGUF

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from sqlmodel import SQLModel

from abstract.manager.manager import SQLModelBound
from database.database import Database

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

GRANITE = r"C:\Users\George\.cache\lm-studio\models\lmstudio-community\granite-3.1-8b-instruct-GGUF\granite-3.1-8b-instruct-Q4_K_M.gguf"

llm = LlamaCpp(
    model_path=GRANITE,
    temperature=0.75,
    max_tokens=2000,
    n_ctx=2048,
    top_p=1,
    # callback_manager=callback_manager,
    # verbose=True,  # Verbose is required to pass to the callback manager
    verbose=False,
)

if __name__ == '__main__':
    import model.comprehensive
    from sqlalchemy.schema import CreateTable

    db = Database()
    sql_statements = []
    tables = SQLModel.metadata.tables.values()
    for table in tables:
        sql = str(CreateTable(table).compile(db.get_engine())).replace("\n", "").replace("\t", "")
        sql_statements.append(sql)

    statement = ';\n'.join(sql_statements)
    print(statement)

    question = """
        CREATE TABLE GICSSector (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY (id), UNIQUE (name));
        CREATE TABLE GICSIndustryGroup (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, sector_id INTEGER NOT NULL, PRIMARY KEY (id), UNIQUE (name), FOREIGN KEY(sector_id) REFERENCES GICSSector (id));
        CREATE TABLE GICSIndustry (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, sector_id INTEGER NOT NULL, industry_group_id INTEGER NOT NULL, PRIMARY KEY (id), UNIQUE (name), FOREIGN KEY(sector_id) REFERENCES GICSSector (id), FOREIGN KEY(industry_group_id) REFERENCES GICSIndustryGroup (id));
        CREATE TABLE GICSSubIndustry (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, sector_id INTEGER NOT NULL, industry_group_id INTEGER NOT NULL, industry_id INTEGER NOT NULL, PRIMARY KEY (id), UNIQUE (name), FOREIGN KEY(sector_id) REFERENCES GICSSector (id), FOREIGN KEY(industry_group_id) REFERENCES GICSIndustryGroup (id), FOREIGN KEY(industry_id) REFERENCES GICSIndustry (id));
        CREATE TABLE currencycountry (currency_id INTEGER NOT NULL, country_id INTEGER NOT NULL, PRIMARY KEY (currency_id, country_id), FOREIGN KEY(currency_id) REFERENCES currency (id), FOREIGN KEY(country_id) REFERENCES country (id));
        CREATE TABLE currency (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, code VARCHAR(255) NOT NULL, symbol VARCHAR(255) NOT NULL, PRIMARY KEY (id), UNIQUE (name));
        CREATE TABLE countrycontinent (country_id INTEGER NOT NULL, continent_id INTEGER NOT NULL, PRIMARY KEY (country_id, continent_id), FOREIGN KEY(country_id) REFERENCES country (id), FOREIGN KEY(continent_id) REFERENCES continent (id));
        CREATE TABLE country (id INTEGER NOT NULL AUTO_INCREMENT, common_name VARCHAR(255) NOT NULL, official_name VARCHAR(255) NOT NULL, cca2 VARCHAR(255) NOT NULL, cca3 VARCHAR(255) NOT NULL, latitude FLOAT, longitude FLOAT, capital VARCHAR(255), population INTEGER NOT NULL, flag_url VARCHAR(255) NOT NULL, PRIMARY KEY (id), UNIQUE (common_name), UNIQUE (official_name), UNIQUE (cca2), UNIQUE (cca3));
        CREATE TABLE exchange (id INTEGER NOT NULL AUTO_INCREMENT, code VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, country_id INTEGER NOT NULL, currency_id INTEGER NOT NULL, PRIMARY KEY (id), UNIQUE (code), FOREIGN KEY(country_id) REFERENCES country (id), FOREIGN KEY(currency_id) REFERENCES currency (id));
        CREATE TABLE ticker (id INTEGER NOT NULL AUTO_INCREMENT, isin VARCHAR(255), code VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, exchange_id INTEGER NOT NULL, currency_id INTEGER NOT NULL, instrument_type ENUM('COMMON_STOCK','ETF') NOT NULL, PRIMARY KEY (id), UNIQUE (isin), FOREIGN KEY(exchange_id) REFERENCES exchange (id), FOREIGN KEY(currency_id) REFERENCES currency (id));
        CREATE TABLE company (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, isin VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL, primary_ticker VARCHAR(255), homepage VARCHAR(255), logo_url VARCHAR(255), employees INTEGER, description VARCHAR(4096) NOT NULL, fiscal_year_end VARCHAR(255) NOT NULL, ticker_id INTEGER, gics_sector_id INTEGER, gics_industry_group_id INTEGER, gics_industry_id INTEGER, gics_subindustry_id INTEGER, currency_id INTEGER, country_id INTEGER NOT NULL, PRIMARY KEY (id), UNIQUE (isin), UNIQUE (primary_ticker), FOREIGN KEY(ticker_id) REFERENCES ticker (id), FOREIGN KEY(gics_sector_id) REFERENCES GICSSector (id), FOREIGN KEY(gics_industry_group_id) REFERENCES GICSIndustryGroup (id), FOREIGN KEY(gics_industry_id) REFERENCES GICSIndustry (id), FOREIGN KEY(gics_subindustry_id) REFERENCES GICSSubIndustry (id), FOREIGN KEY(currency_id) REFERENCES currency (id), FOREIGN KEY(country_id) REFERENCES country (id));
        CREATE TABLE companysnapshotmetrics (id INTEGER NOT NULL AUTO_INCREMENT, market_capitalization NUMERIC(26, 2), enterprise_value NUMERIC(26, 2), return_on_assets FLOAT NOT NULL, operating_profit_margin FLOAT NOT NULL, net_profit_margin FLOAT NOT NULL, updated_at DATE NOT NULL, company_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY(company_id) REFERENCES company (id));
        CREATE TABLE continent (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY (id), UNIQUE (name));
        CREATE TABLE user (id INTEGER NOT NULL AUTO_INCREMENT, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, avatar_url VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), birthdate DATE, PRIMARY KEY (id), UNIQUE (username), UNIQUE (email))
    
        if my schema was created with the model above write me SQL that retrieves all the companies in Germany. Just the SQL string and nothing else.
        """
    import time

    s = time.time()
    print(llm.invoke(question))
    e = time.time()
    print(e - s)
