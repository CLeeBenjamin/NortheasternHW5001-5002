def main():

    print("Welcome to my election calculator!")

    winner = input("Who won?\n")
    loser = input("Who lost?\n")
    winner_votes = float(input("How many votes did the winner receive?\n"))
    loser_votes = float(input("How many votes did the loser receive?\n"))

    total_votes = winner_votes + loser_votes
    print(winner, "got ", winner_votes, "votes out of", total_votes)

    winning_pct = (winner_votes / total_votes) * 100

    print(winner, "got ", winning_pct, "% of the votes ", sep = " ")
    


main()
