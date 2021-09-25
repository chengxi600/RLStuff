import rlgym

env = rlgym.make()

for ep in range(10):
    done = False
    state = env.reset()

    while not done:
        action = env.action_space.sample()

        new_state, reward, done, _ = env.step(action)

        state = new_state

        if done:
            break