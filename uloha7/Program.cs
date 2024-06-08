using System;
using System.Collections.Generic;

class DiceGame
{
    static void Main(string[] args)
    {
        Console.Clear();

        Console.WriteLine("Enter number of players: ");
        int playerCount = int.Parse(Console.ReadLine());
        if (playerCount < 2)
        {
            Console.WriteLine("The minimum number of players is 2!");
            return;
        }
        else if (playerCount > 5)
        {
            Console.WriteLine("The maximum number of players is 5!");
            return;
        }

        GameSession gameSession = new GameSession();
        gameSession.InitializePlayers(playerCount);

        while (true)
        {
            if (gameSession.ExecuteTurn() == 1) break;
        }
    }
}

class Participant
{
    public string playerName;
    public int playerScore;

    public Participant(string playerName)
    {
        this.playerName = playerName;
        playerScore = 0;
    }

    public void AddPoints(int points)
    {
        playerScore += points;
    }

    public int[] RollDiceSet(Dice firstDice, Dice secondDice)
    {
        firstDice.Roll();
        secondDice.Roll();
        return new int[] { firstDice.result, secondDice.result };
    }
}

class Dice
{
    public int result;

    public void Roll()
    {
        Random random = new Random();
        result = random.Next(1, 7);
    }
}

class GameSession
{
    public List<Participant> participants;
    public Dice firstDice;
    public Dice secondDice;
    public const int targetScore = 100;

    public GameSession()
    {
        firstDice = new Dice();
        secondDice = new Dice();
        participants = new List<Participant>();
    }

    public void InitializePlayers(int playerCount)
    {
        for (int i = 0; i < playerCount; i++)
        {
            Console.WriteLine("Enter player name: ");
            string playerName = Console.ReadLine();
            participants.Add(new Participant(playerName));
        }
        Console.Clear();
    }

    private string CheckForWinner()
    {
        foreach (var participant in participants)
        {
            if (participant.playerScore >= targetScore)
            {
                return participant.playerName;
            }
        }
        return string.Empty;
    }

    public int ExecuteTurn()
    {
        foreach (var participant in participants)
        {
            Console.WriteLine($"{participant.playerName} is up next");
            Console.WriteLine("Press any key to roll the dice:");
            Console.ReadKey();
            int[] diceResults = participant.RollDiceSet(firstDice, secondDice);
            Console.WriteLine($"Dice 1: {diceResults[0]}");
            Console.WriteLine($"Dice 2: {diceResults[1]}");

            if (diceResults[0] == 1 && diceResults[1] == 1)
            {
                Console.WriteLine("Rolled a 1 on both dice, you lose all points.");
                participant.playerScore = 0;
            }
            else if (diceResults[0] == 1 || diceResults[1] == 1)
            {
                Console.WriteLine("Rolled a 1 on one die, no points this turn.");
            }
            else
            {
                participant.AddPoints(diceResults[0] + diceResults[1]);
            }

            Console.WriteLine($"{participant.playerName} score: {participant.playerScore}");
            string winner = CheckForWinner();
            if (!string.IsNullOrEmpty(winner))
            {
                Console.WriteLine("--------------------");
                Console.WriteLine($"{winner} WINS!");
                return 1;
            }
            Console.WriteLine("--------------------");
        }
        return 0;
    }
}
