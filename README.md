# black-scholes-TUI
Access a Black-Scholes calculator from your Arch Linux terminal that compares theoretical values to live options prices from Yahoo Finance.

## Features
- Command Line Interface (CLI)
- European call option pricing
- European put option pricing
- Greeks calculation
- Theoretical price comparison against market prices
- 
$$
\huge C = S_0 N(d_1) - K e^{-rT} N(d_2)
$$

$$
\huge P = K e^{-rT} N(-d_2) - S_0 N(-d_1)
$$

  $$
\huge d_1 = \frac{\ln\left(\frac{S_0}{K}\right) + \left(r + \frac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}
$$

$$
\huge d_2 = d_1 - \sigma \sqrt{T}
$$
