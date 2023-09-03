"""Mee Vang 09/02/23  Task 4"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def area_of_pop_can(height, width):
  
    logger.info(f"CALLING area_of_pop_can({height, width})")

    try: 
        area = height * width
        logger.info(f"The circle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    


def sugar_in_pop(mass, volume):

    logger.info(f"Calling sugar_in_pop({mass, volume})")

    try:
        total_sugar = (mass / volume)
        logger.info(f"The total amount of sugar per can is {total_sugar}")
        return total_sugar
    except Exception as ex:
        logger.info(f"Error: {ex}")
        return None


def weekly_consumption(daily, number_of_days):
    logger.info(f"Calling weekly_consumption({daily, number_of_days})")

    try:
        total_weekly = (daily * number_of_days)
        logger.info(f"The total weekly amount of pop is {total_weekly}")
        return total_weekly
    except Exception as ex:
        logger.info(f"Error: {ex}")
        return None


def calories(carbs, protein, fat):
    logger.info(f"Calling weekly_consumption({carbs, protein, fat})")

    try:
        total_cal = ((carbs * 4) + (protein * 4) + (fat * 9))
        logger.info(f"The total weekly amount of pop is {total_cal}")
        return total_cal
    except Exception as ex:
        logger.info(f"Error: {ex}")
        return None


if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info("")

    logger.info("TRY: Call area_of_pop_can() function with a different values.")
    area_of_pop_can(12, 10)
    area_of_pop_can(24, 5)
    logger.info("")


    logger.info("TRY: Call sugar_in_pop() function with a list of different values")
    sugar_in_pop = [7, 15, 21, 30, 40, 59]
    logger.info("")


    logger.info("TRY: Call weekly_consumption() function with different values")
    weekly_consumption(4, 7)
    logger.info("")


    logger.info("TRY: Call calories() function with different values")
    weekly_consumption(10, 59)
    logger.info("")

    print("Done.")

