"""
Service needs to run on schedule (See run_crontab.py)
"""

if __name__ == "__main__":
    try:
        from app.logger.logger import configure_logging

        logger = configure_logging(__name__)

        import asyncio
        from dotenv import load_dotenv

        load_dotenv()

        # from app.api.services.schedule import PredictFlowSchedule

        # asyncio.run(PredictFlowSchedule().start())

        logger.info("Run Crontab Schedule")

    except Exception as e:
        print(e)
