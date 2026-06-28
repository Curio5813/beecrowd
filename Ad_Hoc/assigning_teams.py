def assigning_teams():
    """
    Four friends are playing table tennis. Each of them has a skill
    level which is represented by an integer number: the higher the
    number, the better the player is.

    The four friends want to form two teams of two players each. For the
    game to be more exciting, they want the skill level of the teams to
    be as close as possible. The skill level of a team is the sum of the
    skill levels of the players in that team.

    Although they are very good table tennis players, these friends are not
    so good at other things, like Math or Computing. Can you help them find
    the smallest possible difference between the teams’ skill levels?

    Input
    The input consists of a single line that contains four integers A, B, C
    and D, representing the skill levels of the four players (0 ≤ A ≤ B ≤ C 
    D ≤ 10^4).

    Output
    Output a line with an integer representing the smallest difference between the skill
    levels for both teams.
    :return:
    """
    jogadores = list(map(int, input().split(" ")))
    jogadores.sort()
    diff = abs((jogadores[1] + jogadores[2]) - (jogadores[0] + jogadores[3]))
    print(diff)


assigning_teams()
