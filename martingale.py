"""Assess a betting strategy.                                                               
                                                                
Copyright 2018, Georgia Institute of Technology (Georgia Tech)                                                                
Atlanta, Georgia 30332                                                                
All Rights Reserved                                                         
                                                                
Template code for CS 4646/7646                                                                
                                                                
Georgia Tech asserts copyright ownership of this template and all derivative                                                                
works, including solutions to the projects assigned in this course. Students                                                                
and other users of this template code are advised not to share it with others                                                               
or to make it available on publicly viewable websites including repositories                                                                
such as github and gitlab.  This copyright statement should not be removed                                                                
or edited.                                                                
                                                                
We do grant permission to share solutions privately with non-students such                                                                
as potential employers. However, sharing with other current or future                                                               
students of CS 7646 is prohibited and subject to being investigated as a                                                                
GT honor code violation.                                                                
                                                                
-----do not edit anything above this line---                                                                
                                                                
Student Name: Sarah Hernandez                                                         
GT User ID: shernandez43                                                          
GT ID: 903458532                                                          
"""                                                               
                                                                
import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt                                                               
                                                                
def author():                                                               
   return "shernandez43"                                                               
                                                                
def gtid():                                                               
  return 903458532                                                                
                                                                
def get_spin_result(win_prob):                                                                
  result = False                                                                
  if np.random.random() <= win_prob:                                                                
    result = True 
  return result                                                               
                                                                
def run_episode(ex2):                                                                
  win_prob = 18/38.0 #18 black pockets out of a total of 38                                                            
                                                       
  max_spins = 1001 #starting value + 1000 spins = np array of size 1001
  winnings_history = np.zeros(max_spins)
  winnings = 0
  num_spins = 0

  while winnings < 80 and num_spins < max_spins:
    
    won = False
    bet_amount = 1
    while not won and num_spins < max_spins:

      won = get_spin_result(win_prob)
      num_spins += 1

      if won:
        winnings = winnings + bet_amount
      else:
        winnings = winnings - bet_amount
        bet_amount = bet_amount*2

      if num_spins >= max_spins:
        continue

      winnings_history[num_spins] = winnings

      # corner case:
      if ex2 and bet_amount > 256 + winnings:
        bet_amount = 256 + winnings

      # get out of loop if we break the bank, would like a cleaner way to break out of these two loops.
      if ex2 and winnings <= -256:
        break

    if ex2 and winnings <= -256:
        break

  #if winnings > 80:
  #  print winnings_history

  if num_spins < max_spins:
    winnings_history[num_spins:] = winnings_history[num_spins]

  
  return winnings_history

  



                                                                
  # add your code here to implement the experiments                                                               

def gen_fig1():
  runs = 10
  run_results = []
  x = range(1001)
  for i in range(runs):
    y = run_episode(False)
    run_results.append(y)
    plt.plot(x,y, label = "Episode # " + str(i+1))

  plt.xlim(0, 301)
  plt.ylim(-256, 101)

  plt.xlabel("Spin Number")
  plt.ylabel("Winnings")
  plt.legend()
  plt.title("Figure 1: Winnings over Spins")

  plt.savefig("Figure 1.png")

  
def gen_fig2_and_3():
  runs = 1000
  run_results = []
  x = range(1001)
  for i in range(runs):
    y = run_episode(False)
    run_results.append(y)

  df = pd.DataFrame(data=run_results,    # values
              index=range(len(run_results)),    # index
              columns=range(len(run_results[0])))  #column names are spin #'s


  # Generate Figure 2:
  plt.figure()
  y = df.mean()
  std = df.std()
  make_and_save_fig(x, y, std, "Mean", "Figure 2: Mean Winnings over Spin Number", "Figure 2.png")

 
  # Generate Figure 3:
  plt.figure()
  ymed = df.median()
  make_and_save_fig(x, ymed, std, "Median", "Figure 3: Median Winnings over Spin Number", "Figure 3.png")

  


def gen_fig4_and_5():
  runs = 1000
  run_results = []
  x = range(1001)
  for i in range(runs):
    y = run_episode(True)
    run_results.append(y)

  df = pd.DataFrame(data=run_results,    # values
              index=range(len(run_results)),    # index
              columns=range(len(run_results[0])))  #column names are spin #'s


  # Generate Figure 4:
  plt.figure()
  y = df.mean()
  std = df.std()
  make_and_save_fig(x, y, std, "Mean", "Figure 4: Mean Winnings over Spin Number with $256 Bank Roll", "Figure 4.png")


  print "Mean, bank: ", y.mean(), "Final y: ", y[-1:]
  print "Std, bank: ", std.mean(), " Max Std: ", std.max(), "Final STD: ", std[-1:]
  print "VAL COUNTS: "
  print df[1000].value_counts()

  # Generate Figure 5:
  plt.figure()
  ymed = df.median()
  make_and_save_fig(x, ymed, std, "Median", "Figure 5: Median Winnings over Spin Number with $256 Bank Roll", "Figure 5.png")

  



def make_and_save_fig(x, y, std, type, title, saveName):

  plt.plot(x, y, label = type + " of each spin")
  plt.plot(x, y+std, '-', color = 'r', label = "+1 Standard Deviation")
  plt.plot(x, y-std, '-', color = 'g', label = "-1 Standard Deviation")
  plt.xlim(0, 301)
  plt.ylim(-256, 101)

  plt.xlabel("Spin Number")
  plt.ylabel("Winnings")
  plt.legend()
  plt.title(title)

  plt.savefig(saveName)


if __name__ == "__main__":                                                                
    
    np.random.seed(gtid()) # set seed, run expirements, end program

    gen_fig1()
    gen_fig2_and_3()
    gen_fig4_and_5()

    print "End of Martingale"



















