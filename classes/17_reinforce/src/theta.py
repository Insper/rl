for State, Action, G in zip(States, Actions, DiscountedReturns):
    probs = nn(State)
    dist = torch.distributions.Categorical(probs=probs)
    log_prob = dist.log_prob(Action)

    # importante: aqui deve ser negativo pq eh um gradient ascent
    loss = -log_prob*G

    optim.zero_grad()
    loss.backward()
    optim.step()