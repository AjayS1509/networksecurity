from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig
from networksecurity.components.data_transformation import DataTransformation, DataTransformationConfig
from networksecurity.components.model_trainer import ModelTrainerConfig, ModelTrainer
import sys

if __name__=="__main__":
    try:
        traningconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=traningconfig)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartificat =  data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartificat)
        data_validation_config = DataValidationConfig(training_pipeline_config=traningconfig)
        data_validation = DataValidation(dataingestionartificat,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        data_transformation_config = DataTransformationConfig(training_pipeline_config=traningconfig)
        logging.info("Data Transforamtion Started")
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transfomration Completed")

        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(traningconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model training artifact created")


    except Exception as e:
        raise NetworkSecurityException(e, sys)