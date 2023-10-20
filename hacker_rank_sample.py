#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests

def getTotalGoals(team, year):
    c = 0

    req = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(
        team) + '&page=1').json()
    totalPage = req['total_pages']
    perPage = req['per_page']
    for i in range(1, totalPage + 1):
        req = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(
            team) + '&page=' + str(i)).json()
        try:
            for j in range(0, perPage):
                team1Goal = req['data'][j]['team1goals']
                c += int(team1Goal)
        except:
            pass

    req = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(
        team) + '&page=1').json()
    print(req)
    totalPage = req['total_pages']
    perPage = req['per_page']
    for i in range(1, totalPage + 1):
        req = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(
            team) + '&page=' + str(i)).json()
        try:
            for j in range(0, perPage):
                team1Goal = req['data'][j]['team2goals']
                c += int(team1Goal)
        except:
            pass

    return c

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)


    fptr.write(str(result) + '\n')

    fptr.close()
