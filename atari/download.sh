#!/bin/bash

for games in Enduro Kangaroo MsPacman Assault BankHeist Boxing Asteroids Bowling 
do
	gsutil -m cp -R gs://atari-replay-datasets/dqn/$games . 
done
