# Project Overview
This project involves using Azure Data Factory, Custom Activity, SQL Database, Azure Databricks, and Azure Storage Account to predict stock prices. The aim is to provide a way for investors to predict the stock market by analyzing stock data from various sources.

## Architecture
The project's architecture consists of several components, as described below:

## Data Sources
The project uses CSV files as data sources for stock data. The CSV files are stored in an Azure Data Lake.

## Data Preparation
A Custom Activity in Azure Data Factory is used to merge CSV files into a single file. The merged file is then loaded into a SQL Database using a Copy Activity in Azure Data Factory.

## Data Processing
Azure Databricks is used to process the data and make predictions on the stock prices. The insights and predictions are then stored in an Azure Storage Account Container.

## Deployment
To deploy the project, you will need to follow the steps below:

Create an Azure Data Lake and upload your CSV files to the lake.

Create an Azure SQL Database.

Create an Azure Data Factory pipeline and use a Custom Activity to merge the CSV files. Use a Copy Activity to load the merged CSV file into the SQL Database.

Create an Azure Databricks cluster and use it to process the data and make predictions.

Use the Azure Storage Account Container to store the insights and predictions.

## Dependencies
To use this project, you will need to have the following dependencies installed:

Azure Data Factory
Azure SQL Database
Azure Databricks
Azure Storage Account

## Architecture Diagram

    +---------------------+    +-----------------+     +-----------------+
    |                     |    |                 |     |                 |
    |   Azure Data Lake   |<---|  Azure Data     |<----|  Custom Activity|
    |                     |    |    Factory      |     |                 |
    +---------------------+    +-----------------+     +-----------------+
                                    /        \
                                   /          \
                     +-----------------+   +----------------+
                     |                 |   |                |
                     |  CSV files      |   |  SQL Database  |
                     |                 |   |                |
                     +-----------------+   +----------------+
                                  |                 |
                                  |                 |
                                  |                 |
                    +----------------+    +-----------------+
                    |                |    |                 |
                    | Azure Databricks|<---|  Azure Storage  |
                    |                |    |      Account    |
                    +----------------+    +-----------------+

In this architecture, data sources (CSV files) are stored in an Azure Data Lake. Azure Data Factory is used to merge the CSV files into a single file, which is then loaded into an Azure SQL Database. Azure Databricks processes the data and makes predictions on stock prices, and the insights are stored in an Azure Storage Account Container.

The Custom Activity in Azure Data Factory is responsible for merging the CSV files, while the Copy Activity loads the merged CSV file into the SQL Database. Azure Databricks is used for data processing, while the Azure Storage Account is used for storing the insights out of it.

This architecture provides an efficient way to predict stock prices by analyzing data from various sources, while ensuring that the entire process is automated and scalable.


## Conclusion
This project provides an efficient way to visualize stock prices by analyzing data from various sources. The use of Azure Data Factory, Custom Activity, SQL Database, Azure Databricks, and Azure Storage Account ensures that the entire process is automated and scalable.
