def main():

    print("Welcome to your election results info session")

    winner = input("Who won?")
    loser =  input("Who lost?")

    winner_votes = float(input("What was " + winner + "'s " "number of votes"))
    loser_votes = float(input("What was " + loser + "'s "
                              "number of votes"))


    total_votes = winner_votes + loser_votes
    winning_pct = (winner_votes / total_votes) * 100
    loser_pct = (loser_votes / total_votes) * 100

    print(total_votes)

    print("So, if the total # of votes is", total_votes,",", "that means", winner, "'s", "percentage is", winning_pct, "and", loser, "'s", "percentage is", loser_pct, sep = " ")

main()

