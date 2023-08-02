# PROJECTION_NOTEBOOK:  
## Project Investment for both **Equity AND Rental Property** over a period of time using simple Monte Carlo Simulation

### Equity Assumptions:

1. **Average Return:** The model starts with the assumption that the average nominal return on investment in the S&P 500 is 7% per year, based on historical data.

2. **Inflation Rate:** The model assumes an average annual inflation rate of 3%.

3. **Real Return:** The model calculates the real return, which is the return on investment after adjusting for inflation, by subtracting the inflation rate from the nominal return. In this case, the real return is 4% per year (7% nominal return - 3% inflation).

4. **Standard Deviation:** The model assumes a standard deviation of 20% for the returns on the S&P 500, reflecting the volatility and risk associated with investing in the stock market.

5. **Number of Simulations:** The model uses the Monte Carlo method to account for the uncertainty and randomness inherent in stock market returns. It runs the simulation 10,000 times to generate a range of possible outcomes.

6. **Years for Projection:** The model provides a projection for the default next 10 years based on the above assumptions.

7. **Initial Investment:** The model assumes an initial investment amount of default $1,000,000.

8. **Monthly Contribution:** The model assumes a monthly contribution of default $14,000 to the investment portfolio. This amount is added to the investment each month in addition to any returns from the previous month's investment.

### Rental Investment Assumptions:  

1. **Initial Rent:** The model begins with a total monthly rent of $9,445, which is the sum of all the initial rents.

2. **Average Annual Rent Increase:** The model assumes an average annual rent increase of 2.5%. This means that the rent is expected to increase by 2.5% every year.

3. **Standard Deviation of Rent Increase:** The rent increase is not fixed and can vary. The model uses a standard deviation of 1% to simulate this variation.

4. **Annual Maintenance Cost Rate:** The model assumes that the annual cost for maintaining the property is 1% of the property value.

5. **Initial Property Value:** The model starts with a total property value of the initial property values.

6. **Average Annual Property Appreciation:** The model assumes an average annual property appreciation of 4%. This means that the property value is expected to increase by 4% every year.

7. **Standard Deviation of Property Appreciation:** The property appreciation is not fixed and can vary. The model uses a standard deviation of 1.5% to simulate this variation.

8. **Expected Vacancy Rate:** The model assumes a vacancy rate of 10%. This means that, on average, 10% of the properties are expected to be vacant and not generating any rent.

9. **Tax Rate on Rental Income:** The model assumes a tax rate of 30% on rental income.

10. **Inflation Rate:** The model uses an inflation rate based on a predefined variable named `INFLATION_RATE`. This rate is expected to affect both the rents and property values.

11. **Years for Projection:** The model provides a projection for the next 10 years.

12. **Number of Monte Carlo Simulations:** To account for the inherent randomness and uncertainties in the projections, the model uses a Monte Carlo method. It runs the simulation 10,000 times to generate a range of possible outcomes.

# Portfolio Analysis Notebook


## Overview

This script is designed to visualize and compare the growth of an investment over time for a specified portfolio and market indices, such as the S&P 500 and Dow Jones Industrial Average. Users can define a portfolio with specific weightings in different ETFs and then see how a hypothetical initial investment, with a regular monthly addition, would grow over a specified time frame.

## Features

- **Fetch Historical Data**: Downloads the historical price data for a given portfolio and market indices.
- **Calculate Returns**: Computes the daily returns for both the portfolio and the market indices.
- **Apply Monthly Investment**: Applies a user-defined monthly investment to the total.
- **Visualize Growth**: Plots the cumulative investment value over time for both the portfolio and the market indices.


## Usage

1. **Define Portfolio**: In the script, specify the portfolio by defining the tickers and their respective weights in the `portfolio_1` dictionary.
2. **Define Market Indices**: Define the market indices that you want to compare against in the `stocks` dictionary.
3. **Set Initial Investment and Monthly Contribution**: Modify the `initial_investment` and `monthly_investment` variables in the `compute_investment` function if you want to change the default values of $100,000 and $500, respectively.


5. **View the Plot**: The script will display a plot showing the investment growth over time for both the portfolio and the selected market indices.
