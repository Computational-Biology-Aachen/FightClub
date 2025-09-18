def deriv(y, t, nu, beta, alpha, r_p, r_m, gamma, eta):
    P, C, M = y
    dPdt = r_p * P - alpha * C * P - beta * M * P - eta * P * P  # Public population
    dCdt = -nu * C * C + alpha * P * C  # cheater population
    dMdt = r_m * M - beta * M * P - gamma * M * M  # private population
    return dPdt, dCdt, dMdt