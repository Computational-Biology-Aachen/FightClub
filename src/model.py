def deriv(y, t, nu, beta, alpha, r_c, r_p, gamma, eta):
    C, D, P = y
    dCdt = r_c * C - alpha * C * D - beta * C * P - eta * C * C  # cooperator population
    dDdt = -nu * D * D + alpha * C * D  # defector population
    dPdt = r_p * P - beta * C * P - gamma * P * P  # private population
    return dCdt, dDdt, dPdt