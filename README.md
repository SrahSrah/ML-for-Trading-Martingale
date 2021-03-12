# ML-for-Trading-Martingale
Explore betting simulation as a means of exploiting stock market variations

**Martingale Report** 

**By: Sarah Hernandez** 

**Question 1:** 

Given an unlimited bank roll, the probability of attaining $80 in winnings is greater than 99%. As you can see in Figures 1 and 2, the player will attain $80 after about 200 spins on average. Further proof of this can be found by looking at the +/- standard deviation lines in Figures 2 and 3. As the number of spins increases, the standard deviation converges to 0, resulting in these lines converging on the $80 mark. 

**Question 2:** 

Given the $80 cap, the expected value of our winnings after 1000 bets 

is $80, as $80 was reached in each of our 1000 simulations. However, should we remove this constraint, our expected winnings after 1000 bets is around $473.68. Using the expected value equation below, we get the following: 

<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.001.png" />
</p>

- E(X) = ($1\*(18/38))\*1000 spins = $473.68 

This is because we have a 18/38 chance to win $1 after each spin. Here, given the unlimited bank roll, we can virtually ignore the possibility for losses as we're instructed to spin until we win, whereupon we are almost back on track to achieve our targeted value. Indeed, if you remove the $80 cap in the code, each trail of 100 bets hovers around the $473.68 value. I imagine, however, that we cannot ignore the affect of losses entirely and that the real expected value is slightly lower that $473.68 given no winnings cap. 

**Question 3:** 

Given the $80 winnings cap, the standard deviation does reach a maximum value, but does not stabilize. Rather, it reaches a maximum value and then converges to 0 as the number of bets increases. Without the winnings cap, the standard deviation would to vary widely from spin to spin. This is because with an unlimited bank roll, the possible winnings values at each spin varies far more widely. 

**Question 4:** 

First, based off the median values show in Figure 5, we know that achieving $80 in winnings will occur more than half of the time. 

Subsequently, after generating the data for Figures 4 and 5, I ran a value\_counts() operation on the resultant dataframe. Because of the nature of our spinner, the only two winnings values after 1000 spins are $80 and - $256. Eighty dollars was reached 671 times out of 1000 spins, or about 63% of the time. We can thus conclude that we can expect to reach $80 about 63% of the time. 

While this is higher than I personally expected, it makes sense given the $256 bank roll, allowing us to lose numerous times in a row before getting into real trouble. A smaller bank roll would reduce our chance of reaching $80, and vice versa. 

**Question 5:** 

As you can see in Figure 4, the mean winnings with a limited bank roll eventually converges to a value of about -$44.66 Indeed, if we use the above equation and our results from question 4, we get: 

- E(X) = (-256)(0.37) + (80)(0.63) = -44.32 

-$44.32 is remarkably close to the -$44.66 we got in our trial run. Thus, we can conclude that the expected value of our winnings after 1000 bets is around -$44.50. 

**Question 6:** 

In Experiment 2, as the spin number increases, the standard deviation does indeed increase to a maximum value and then stabilizes around the 175th spin. This is because we have both an upper and lower limit to our winnings values, restricting the number of possible values we can have in our winnings columns in the first place. As such, the standard deviation stabilizes, in our case, around 162.39. We already stated that as the number of spins increases, the winnings will converge to one of two 

values: $80 or -$256. The standard deviation of these two numbers alone is 168, close to our experimental value, indicating that we are on the right track. 

**Question 7: Figures:**
<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.001.png" />
</p>
<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.002.png" />
</p>
<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.003.png" />
</p>
<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.004.png" />
</p>
<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.005.png" />
</p>
<p align="center">
  <img src="Aspose.Words.4720bf56-e6cd-4ff6-b182-1c21f6a5879e.006.png" />
</p>
