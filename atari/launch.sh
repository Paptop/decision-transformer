search_dir=`ls ./dqn_replay/`
for entry in $search_dir
do
	python run_dt_atari.py --seed 127 --context_length 30 --epochs 1 --model_type 'reward_conditioned' --num_steps 50000 --num_buffers 50 --game $entry --batch_size 128 --comment "TestRunAllGames"
done
