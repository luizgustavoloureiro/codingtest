#IMPORTING THE LIBRARIES USED IN DEVELOPMENT

import pandas as pd

#DECLARING TICKERS OF PORTOFOLIO"
Tickers=["CAML3","CPLE6","EMBR3","ITUB3","JHSF3","MRFG3","PCAR3","PETR4","ROMI3","VALE3"]

#DATAS FROM STOCKS, DATE AND CLOSE PRICE FROM 09/01/2021 TO 12/30/2021
#M0 IS THE MONTH(September) THAT WILL BASE THE INITIAL DELTAS OF PORTOFOLIO
#THE REBALANCE IS WILL EVERY MONTH AND THE PROXY OF RISK WILL BE THE DEVIATION OF EACH MONTH
#VARIABLES WITH OPEN IS THE PRICE OPEN IN DAYS OF REBALANCE THE PORTOFOLIO

CAML3_M0=[['Sep 30, 2021', 9.87], ['Sep 29, 2021', 9.71], ['Sep 28, 2021', 9.72], ['Sep 27, 2021', 10.07], ['Sep 24, 2021', 9.61], ['Sep 23, 2021', 9.6], ['Sep 22, 2021', 9.56], ['Sep 21, 2021', 9.52], ['Sep 20, 2021', 9.39], ['Sep 17, 2021', 9.55], ['Sep 16, 2021', 9.53], ['Sep 15, 2021', 9.35], ['Sep 14, 2021', 9.64], ['Sep 13, 2021', 9.4], ['Sep 10, 2021', 9.09], ['Sep 09, 2021', 9.25], ['Sep 08, 2021', 9.18], ['Sep 06, 2021', 9.44], ['Sep 03, 2021', 9.28], ['Sep 02, 2021', 9.58], ['Sep 01, 2021', 9.8]]
CAML3_M1_OPEN=['Oct 01, 2021', 10.05]
CAML3_M1=[['Oct 29, 2021', 9.68], ['Oct 28, 2021', 9.81], ['Oct 27, 2021', 9.68], ['Oct 26, 2021', 9.67], ['Oct 25, 2021', 9.9], ['Oct 22, 2021', 9.75], ['Oct 21, 2021', 9.92], ['Oct 20, 2021', 9.86], ['Oct 19, 2021', 10.24], ['Oct 18, 2021', 10.24], ['Oct 15, 2021', 10.2], ['Oct 14, 2021', 10.13], ['Oct 13, 2021', 10.05], ['Oct 11, 2021', 9.57], ['Oct 08, 2021', 9.53], ['Oct 07, 2021', 9.59], ['Oct 06, 2021', 9.65], ['Oct 05, 2021', 9.94], ['Oct 04, 2021', 10.08], ['Oct 01, 2021', 10.36]]
CAML3_M2_OPEN=['Nov 01, 2021', 9.79]
CAML3_M2=[['Nov 30, 2021', 9.57], ['Nov 29, 2021', 9.4], ['Nov 26, 2021', 9.5], ['Nov 25, 2021', 9.4], ['Nov 24, 2021', 9.37], ['Nov 23, 2021', 9.47], ['Nov 22, 2021', 9.37], ['Nov 19, 2021', 9.57], ['Nov 18, 2021', 9.62], ['Nov 17, 2021', 9.83], ['Nov 16, 2021', 10.15], ['Nov 12, 2021', 10.17], ['Nov 11, 2021', 10.36], ['Nov 10, 2021', 10.3], ['Nov 09, 2021', 10.25], ['Nov 08, 2021', 10.3], ['Nov 05, 2021', 10.06], ['Nov 04, 2021', 10.5], ['Nov 03, 2021', 10.24], ['Nov 01, 2021', 9.76]]
CAML3_M3_OPEN=['Dec 01, 2021', 9.62]
CAML3_M3=[['Dec 30, 2021', 11.38], ['Dec 29, 2021', 11.02], ['Dec 28, 2021', 10.98], ['Dec 27, 2021', 9.88], ['Dec 23, 2021', 10.09], ['Dec 22, 2021', 10.01], ['Dec 21, 2021', 10.17], ['Dec 20, 2021', 10.18], ['Dec 17, 2021', 10.21], ['Dec 16, 2021', 10.31], ['Dec 15, 2021', 9.94], ['Dec 14, 2021', 9.97], ['Dec 13, 2021', 9.79], ['Dec 10, 2021', 9.73], ['Dec 09, 2021', 9.74], ['Dec 08, 2021', 9.82], ['Dec 07, 2021', 9.77], ['Dec 06, 2021', 9.53], ['Dec 03, 2021', 9.62], ['Dec 02, 2021', 9.42], ['Dec 01, 2021', 9.42]]
CPLE6_M0=[['Sep 30, 2021', 7.28], ['Sep 29, 2021', 7.31], ['Sep 28, 2021', 7.12], ['Sep 27, 2021', 7.21], ['Sep 24, 2021', 7.18], ['Sep 23, 2021', 7.22], ['Sep 22, 2021', 7.15], ['Sep 21, 2021', 6.95], ['Sep 20, 2021', 6.94], ['Sep 17, 2021', 6.63], ['Sep 16, 2021', 6.87], ['Sep 15, 2021', 6.94], ['Sep 14, 2021', 7.13], ['Sep 13, 2021', 7.13], ['Sep 10, 2021', 7.05], ['Sep 09, 2021', 7.06], ['Sep 08, 2021', 6.8], ['Sep 06, 2021', 7.13], ['Sep 03, 2021', 6.79], ['Sep 02, 2021', 6.98], ['Sep 01, 2021', 7.1]]
CPLE6_M1_OPEN=['Oct 01, 2021', 6.67]
CPLE6_M1=[['Oct 29, 2021', 5.92], ['Oct 28, 2021', 6.01], ['Oct 27, 2021', 6.07], ['Oct 26, 2021', 6.07], ['Oct 25, 2021', 6.2], ['Oct 22, 2021', 6.18], ['Oct 21, 2021', 6.37], ['Oct 20, 2021', 6.62], ['Oct 19, 2021', 6.64], ['Oct 18, 2021', 6.76], ['Oct 15, 2021', 6.62], ['Oct 14, 2021', 6.5], ['Oct 13, 2021', 6.55], ['Oct 11, 2021', 6.48], ['Oct 08, 2021', 6.65], ['Oct 07, 2021', 6.51], ['Oct 06, 2021', 6.56], ['Oct 05, 2021', 6.55], ['Oct 04, 2021', 6.64], ['Oct 01, 2021', 6.8]]
CPLE6_M2_OPEN=['Nov 01, 2021', 6.02]
CPLE6_M2=[['Nov 30, 2021', 6.14], ['Nov 29, 2021', 6.1], ['Nov 26, 2021', 6.05], ['Nov 25, 2021', 6.16], ['Nov 24, 2021', 6.11], ['Nov 23, 2021', 6.22], ['Nov 22, 2021', 6.11], ['Nov 19, 2021', 6.21], ['Nov 18, 2021', 6.09], ['Nov 17, 2021', 6.09], ['Nov 16, 2021', 6.18], ['Nov 12, 2021', 6.24], ['Nov 11, 2021', 6.3], ['Nov 10, 2021', 6.28], ['Nov 09, 2021', 6.2], ['Nov 08, 2021', 5.96], ['Nov 05, 2021', 5.96], ['Nov 04, 2021', 5.98], ['Nov 03, 2021', 6.09], ['Nov 01, 2021', 5.95]]
CPLE6_M3_OPEN=['Dec 01, 2021', 6.15]
CPLE6_M3=[['Dec 30, 2021', 6.44], ['Dec 29, 2021', 6.4], ['Dec 28, 2021', 6.4], ['Dec 27, 2021', 6.42], ['Dec 23, 2021', 6.32], ['Dec 22, 2021', 6.32], ['Dec 21, 2021', 6.27], ['Dec 20, 2021', 6.31], ['Dec 17, 2021', 6.42], ['Dec 16, 2021', 6.36], ['Dec 15, 2021', 6.44], ['Dec 14, 2021', 6.39], ['Dec 13, 2021', 6.43], ['Dec 10, 2021', 6.42], ['Dec 09, 2021', 6.36], ['Dec 08, 2021', 6.35], ['Dec 07, 2021', 6.24], ['Dec 06, 2021', 6.14], ['Dec 03, 2021', 6.21], ['Dec 02, 2021', 6.27], ['Dec 01, 2021', 6.11]]
EMBR3_M0=[['Sep 30, 2021', 23.13], ['Sep 29, 2021', 23.57], ['Sep 28, 2021', 23.07], ['Sep 27, 2021', 23.53], ['Sep 24, 2021', 23.86], ['Sep 23, 2021', 23.89], ['Sep 22, 2021', 21.3], ['Sep 21, 2021', 20.21], ['Sep 20, 2021', 20.36], ['Sep 17, 2021', 20.88], ['Sep 16, 2021', 21.25], ['Sep 15, 2021', 21.44], ['Sep 14, 2021', 21.33], ['Sep 13, 2021', 21.87], ['Sep 10, 2021', 21.18], ['Sep 09, 2021', 21.63], ['Sep 08, 2021', 21.07], ['Sep 06, 2021', 21.55], ['Sep 03, 2021', 21.76], ['Sep 02, 2021', 22.78], ['Sep 01, 2021', 22.93]]
EMBR3_M1_OPEN=['Oct 01, 2021', 23.35]
EMBR3_M1=[['Oct 29, 2021', 21.93], ['Oct 28, 2021', 22.37], ['Oct 27, 2021', 22.49], ['Oct 26, 2021', 23.17], ['Oct 25, 2021', 24.12], ['Oct 22, 2021', 24.25], ['Oct 21, 2021', 24.13], ['Oct 20, 2021', 24.65], ['Oct 19, 2021', 24.94], ['Oct 18, 2021', 25.66], ['Oct 15, 2021', 25.68], ['Oct 14, 2021', 26.05], ['Oct 13, 2021', 25.9], ['Oct 11, 2021', 25.96], ['Oct 08, 2021', 24.75], ['Oct 07, 2021', 24.09], ['Oct 06, 2021', 23.38], ['Oct 05, 2021', 22.96], ['Oct 04, 2021', 24.05], ['Oct 01, 2021', 24.27]]
EMBR3_M2_OPEN=['Nov 01, 2021', 22.09]
EMBR3_M2=[['Nov 30, 2021', 19.14], ['Nov 29, 2021', 19.75], ['Nov 26, 2021', 19.27], ['Nov 25, 2021', 21.04], ['Nov 24, 2021', 20.6], ['Nov 23, 2021', 20.59], ['Nov 22, 2021', 20.37], ['Nov 19, 2021', 20.72], ['Nov 18, 2021', 21.06], ['Nov 17, 2021', 20.95], ['Nov 16, 2021', 21.5], ['Nov 12, 2021', 21.97], ['Nov 11, 2021', 22.99], ['Nov 10, 2021', 22.64], ['Nov 09, 2021', 23.37], ['Nov 08, 2021', 22.88], ['Nov 05, 2021', 23.11], ['Nov 04, 2021', 21.71], ['Nov 03, 2021', 22.35], ['Nov 01, 2021', 22.33]]
EMBR3_M3_OPEN=['Dec 01, 2021', 19.8]
EMBR3_M3=[['Dec 30, 2021', 24.82], ['Dec 29, 2021', 24.42], ['Dec 28, 2021', 24.49], ['Dec 27, 2021', 24.44], ['Dec 23, 2021', 24.35], ['Dec 22, 2021', 23.6], ['Dec 21, 2021', 23.1], ['Dec 20, 2021', 19.91], ['Dec 17, 2021', 20.4], ['Dec 16, 2021', 20.57], ['Dec 15, 2021', 20.72], ['Dec 14, 2021', 20.63], ['Dec 13, 2021', 20.64], ['Dec 10, 2021', 21.42], ['Dec 09, 2021', 20.76], ['Dec 08, 2021', 21.3], ['Dec 07, 2021', 20.3], ['Dec 06, 2021', 20.23], ['Dec 03, 2021', 19.15], ['Dec 02, 2021', 19.36], ['Dec 01, 2021', 18.3]]
ITUB3_M0=[['Sep 30, 2021', 27.0], ['Sep 29, 2021', 26.92], ['Sep 28, 2021', 26.51], ['Sep 27, 2021', 27.19], ['Sep 24, 2021', 26.49], ['Sep 23, 2021', 26.85], ['Sep 22, 2021', 25.97], ['Sep 21, 2021', 25.36], ['Sep 20, 2021', 25.38], ['Sep 17, 2021', 25.86], ['Sep 16, 2021', 26.58], ['Sep 15, 2021', 26.56], ['Sep 14, 2021', 26.93], ['Sep 13, 2021', 27.15], ['Sep 10, 2021', 26.8], ['Sep 09, 2021', 26.98], ['Sep 08, 2021', 26.59], ['Sep 06, 2021', 28.09], ['Sep 03, 2021', 27.48], ['Sep 02, 2021', 27.98], ['Sep 01, 2021', 29.12]]
ITUB3_M1_OPEN=['Oct 01, 2021', 27.05]
ITUB3_M1=[['Oct 29, 2021', 21.03], ['Oct 28, 2021', 21.45], ['Oct 27, 2021', 21.59], ['Oct 26, 2021', 21.52], ['Oct 25, 2021', 21.72], ['Oct 22, 2021', 21.24], ['Oct 21, 2021', 22.06], ['Oct 20, 2021', 22.35], ['Oct 19, 2021', 21.78], ['Oct 18, 2021', 22.36], ['Oct 15, 2021', 22.1], ['Oct 14, 2021', 21.68], ['Oct 13, 2021', 21.85], ['Oct 11, 2021', 21.87], ['Oct 08, 2021', 22.31], ['Oct 07, 2021', 22.19], ['Oct 06, 2021', 22.54], ['Oct 05, 2021', 22.4], ['Oct 04, 2021', 22.26], ['Oct 01, 2021', 27.85]]
ITUB3_M2_OPEN=['Nov 01, 2021', 21.22]
ITUB3_M2=[['Nov 30, 2021', 20.1], ['Nov 29, 2021', 20.28], ['Nov 26, 2021', 20.36], ['Nov 25, 2021', 20.83], ['Nov 24, 2021', 20.65], ['Nov 23, 2021', 20.11], ['Nov 22, 2021', 19.94], ['Nov 19, 2021', 20.23], ['Nov 18, 2021', 20.27], ['Nov 17, 2021', 20.62], ['Nov 16, 2021', 20.65], ['Nov 12, 2021', 20.88], ['Nov 11, 2021', 20.91], ['Nov 10, 2021', 20.9], ['Nov 09, 2021', 20.39], ['Nov 08, 2021', 20.61], ['Nov 05, 2021', 20.66], ['Nov 04, 2021', 20.92], ['Nov 03, 2021', 22.01], ['Nov 01, 2021', 21.77]]
ITUB3_M3_OPEN=['Dec 01, 2021', 20.14]
ITUB3_M3=[['Dec 30, 2021', 19.09], ['Dec 29, 2021', 19.32], ['Dec 28, 2021', 19.38], ['Dec 27, 2021', 19.45], ['Dec 23, 2021', 19.27], ['Dec 22, 2021', 19.19], ['Dec 21, 2021', 19.01], ['Dec 20, 2021', 19.08], ['Dec 17, 2021', 19.31], ['Dec 16, 2021', 19.76], ['Dec 15, 2021', 19.56], ['Dec 14, 2021', 19.61], ['Dec 13, 2021', 19.52], ['Dec 10, 2021', 19.96], ['Dec 09, 2021', 19.95], ['Dec 08, 2021', 20.41], ['Dec 07, 2021', 20.6], ['Dec 06, 2021', 20.88], ['Dec 03, 2021', 20.7], ['Dec 02, 2021', 20.66], ['Dec 01, 2021', 20.01]]
JHSF3_M0=[['Sep 30, 2021', 5.92], ['Sep 29, 2021', 5.95], ['Sep 28, 2021', 6.06], ['Sep 27, 2021', 6.27], ['Sep 24, 2021', 6.29], ['Sep 23, 2021', 6.32], ['Sep 22, 2021', 6.4], ['Sep 21, 2021', 6.37], ['Sep 20, 2021', 6.23], ['Sep 17, 2021', 6.23], ['Sep 16, 2021', 6.24], ['Sep 15, 2021', 6.29], ['Sep 14, 2021', 6.4], ['Sep 13, 2021', 6.41], ['Sep 10, 2021', 6.17], ['Sep 09, 2021', 6.27], ['Sep 08, 2021', 6.06], ['Sep 06, 2021', 6.4], ['Sep 03, 2021', 6.23], ['Sep 02, 2021', 6.3], ['Sep 01, 2021', 6.55]]
JHSF3_M1_OPEN=['Oct 01, 2021', 5.85]
JHSF3_M1=[['Oct 29, 2021', 4.99], ['Oct 28, 2021', 5.11], ['Oct 27, 2021', 5.36], ['Oct 26, 2021', 5.26], ['Oct 25, 2021', 5.58], ['Oct 22, 2021', 5.38], ['Oct 21, 2021', 5.59], ['Oct 20, 2021', 5.73], ['Oct 19, 2021', 5.77], ['Oct 18, 2021', 6.11], ['Oct 15, 2021', 5.95], ['Oct 14, 2021', 6.13], ['Oct 13, 2021', 6.15], ['Oct 11, 2021', 5.93], ['Oct 08, 2021', 5.88], ['Oct 07, 2021', 5.54], ['Oct 06, 2021', 5.64], ['Oct 05, 2021', 5.83], ['Oct 04, 2021', 5.91], ['Oct 01, 2021', 6.11]]
JHSF3_M2_OPEN=['Nov 01, 2021', 5.08]
JHSF3_M2=[['Nov 30, 2021', 4.7], ['Nov 29, 2021', 4.88], ['Nov 26, 2021', 4.92], ['Nov 25, 2021', 5.07], ['Nov 24, 2021', 4.96], ['Nov 23, 2021', 4.93], ['Nov 22, 2021', 4.83], ['Nov 19, 2021', 5.18], ['Nov 18, 2021', 5.07], ['Nov 17, 2021', 5.02], ['Nov 16, 2021', 5.18], ['Nov 12, 2021', 5.48], ['Nov 11, 2021', 5.65], ['Nov 10, 2021', 5.57], ['Nov 09, 2021', 5.43], ['Nov 08, 2021', 5.34], ['Nov 05, 2021', 5.51], ['Nov 04, 2021', 5.36], ['Nov 03, 2021', 5.44], ['Nov 01, 2021', 5.24]]
JHSF3_M3_OPEN=['Dec 01, 2021', 4.83]
JHSF3_M3=[['Dec 30, 2021', 5.58], ['Dec 29, 2021', 5.49], ['Dec 28, 2021', 5.59], ['Dec 27, 2021', 5.54], ['Dec 23, 2021', 5.41], ['Dec 22, 2021', 5.39], ['Dec 21, 2021', 5.36], ['Dec 20, 2021', 5.51], ['Dec 17, 2021', 5.56], ['Dec 16, 2021', 5.56], ['Dec 15, 2021', 5.61], ['Dec 14, 2021', 5.52], ['Dec 13, 2021', 5.6], ['Dec 10, 2021', 5.7], ['Dec 09, 2021', 5.42], ['Dec 08, 2021', 5.54], ['Dec 07, 2021', 5.31], ['Dec 06, 2021', 5.42], ['Dec 03, 2021', 5.19], ['Dec 02, 2021', 5.02], ['Dec 01, 2021', 4.63]]
MRFG3_M0=[['Sep 30, 2021', 25.66], ['Sep 29, 2021', 25.32], ['Sep 28, 2021', 24.34], ['Sep 27, 2021', 24.28], ['Sep 24, 2021', 22.66], ['Sep 23, 2021', 22.41], ['Sep 22, 2021', 21.46], ['Sep 21, 2021', 21.24], ['Sep 20, 2021', 20.85], ['Sep 17, 2021', 21.22], ['Sep 16, 2021', 21.63], ['Sep 15, 2021', 21.41], ['Sep 14, 2021', 21.51], ['Sep 13, 2021', 21.39], ['Sep 10, 2021', 22.98], ['Sep 09, 2021', 22.43], ['Sep 08, 2021', 21.86], ['Sep 06, 2021', 21.89], ['Sep 03, 2021', 21.34], ['Sep 02, 2021', 21.03], ['Sep 01, 2021', 21.49]]
MRFG3_M1_OPEN=['Oct 01, 2021', 25.65]
MRFG3_M1=[['Oct 29, 2021', 26.5], ['Oct 28, 2021', 25.16], ['Oct 27, 2021', 25.27], ['Oct 26, 2021', 24.61], ['Oct 25, 2021', 24.82], ['Oct 22, 2021', 25.12], ['Oct 21, 2021', 25.29], ['Oct 20, 2021', 25.68], ['Oct 19, 2021', 26.02], ['Oct 18, 2021', 26.49], ['Oct 15, 2021', 27.15], ['Oct 14, 2021', 27.7], ['Oct 13, 2021', 27.06], ['Oct 11, 2021', 26.36], ['Oct 08, 2021', 26.15], ['Oct 07, 2021', 25.71], ['Oct 06, 2021', 26.04], ['Oct 05, 2021', 26.23], ['Oct 04, 2021', 25.85], ['Oct 01, 2021', 25.8]]
MRFG3_M2_OPEN=['Nov 01, 2021', 26.95]
MRFG3_M2=[['Nov 30, 2021', 23.57], ['Nov 29, 2021', 23.88], ['Nov 26, 2021', 23.7], ['Nov 25, 2021', 24.45], ['Nov 24, 2021', 25.17], ['Nov 23, 2021', 25.72], ['Nov 22, 2021', 25.05], ['Nov 19, 2021', 25.89], ['Nov 18, 2021', 25.99], ['Nov 17, 2021', 25.43], ['Nov 16, 2021', 25.71], ['Nov 12, 2021', 26.51], ['Nov 11, 2021', 26.15], ['Nov 10, 2021', 26.0], ['Nov 09, 2021', 26.84], ['Nov 08, 2021', 26.88], ['Nov 05, 2021', 26.37], ['Nov 04, 2021', 26.78], ['Nov 03, 2021', 25.85], ['Nov 01, 2021', 25.44]]
MRFG3_M3_OPEN=['Dec 01, 2021', 23.83]
MRFG3_M3=[['Dec 30, 2021', 22.07], ['Dec 29, 2021', 22.92], ['Dec 28, 2021', 22.78], ['Dec 27, 2021', 22.27], ['Dec 23, 2021', 22.73], ['Dec 22, 2021', 21.82], ['Dec 21, 2021', 23.39], ['Dec 20, 2021', 23.33], ['Dec 17, 2021', 23.78], ['Dec 16, 2021', 22.93], ['Dec 15, 2021', 23.26], ['Dec 14, 2021', 23.57], ['Dec 13, 2021', 22.07], ['Dec 10, 2021', 22.02], ['Dec 09, 2021', 22.0], ['Dec 08, 2021', 22.59], ['Dec 07, 2021', 21.25], ['Dec 06, 2021', 20.85], ['Dec 03, 2021', 20.87], ['Dec 02, 2021', 22.14], ['Dec 01, 2021', 21.87]]
PCAR3_M0=[['Sep 30, 2021', 25.74], ['Sep 29, 2021', 25.23], ['Sep 28, 2021', 25.67], ['Sep 27, 2021', 26.82], ['Sep 24, 2021', 27.46], ['Sep 23, 2021', 26.64], ['Sep 22, 2021', 26.12], ['Sep 21, 2021', 26.29], ['Sep 20, 2021', 25.7], ['Sep 17, 2021', 26.5], ['Sep 16, 2021', 26.86], ['Sep 15, 2021', 27.5], ['Sep 14, 2021', 28.0], ['Sep 13, 2021', 27.81], ['Sep 10, 2021', 27.33], ['Sep 09, 2021', 28.12], ['Sep 08, 2021', 26.6], ['Sep 06, 2021', 28.94], ['Sep 03, 2021', 27.11], ['Sep 02, 2021', 27.09], ['Sep 01, 2021', 27.85]]
PCAR3_M1_OPEN=['Oct 01, 2021', 25.71]
PCAR3_M1=[['Oct 29, 2021', 25.53], ['Oct 28, 2021', 25.71], ['Oct 27, 2021', 25.83], ['Oct 26, 2021', 25.93], ['Oct 25, 2021', 26.92], ['Oct 22, 2021', 26.31], ['Oct 21, 2021', 27.56], ['Oct 20, 2021', 28.87], ['Oct 19, 2021', 28.82], ['Oct 18, 2021', 28.96], ['Oct 15, 2021', 30.96], ['Oct 14, 2021', 27.68], ['Oct 13, 2021', 27.64], ['Oct 11, 2021', 25.9], ['Oct 08, 2021', 24.6], ['Oct 07, 2021', 25.0], ['Oct 06, 2021', 25.52], ['Oct 05, 2021', 25.3], ['Oct 04, 2021', 23.69], ['Oct 01, 2021', 25.08]]
PCAR3_M2_OPEN=['Nov 01, 2021', 25.73]
PCAR3_M2=[['Nov 30, 2021', 22.4], ['Nov 29, 2021', 23.09], ['Nov 26, 2021', 23.15], ['Nov 25, 2021', 23.7], ['Nov 24, 2021', 23.19], ['Nov 23, 2021', 23.05], ['Nov 22, 2021', 22.79], ['Nov 19, 2021', 22.86], ['Nov 18, 2021', 22.5], ['Nov 17, 2021', 22.81], ['Nov 16, 2021', 23.82], ['Nov 12, 2021', 23.48], ['Nov 11, 2021', 23.81], ['Nov 10, 2021', 23.82], ['Nov 09, 2021', 23.51], ['Nov 08, 2021', 23.04], ['Nov 05, 2021', 23.2], ['Nov 04, 2021', 22.89], ['Nov 03, 2021', 24.8], ['Nov 01, 2021', 25.92]]
PCAR3_M3_OPEN=['Dec 01, 2021', 22.64]
PCAR3_M3=[['Dec 30, 2021', 21.73], ['Dec 29, 2021', 21.8], ['Dec 28, 2021', 22.58], ['Dec 27, 2021', 22.16], ['Dec 23, 2021', 22.19], ['Dec 22, 2021', 22.14], ['Dec 21, 2021', 22.62], ['Dec 20, 2021', 22.65], ['Dec 17, 2021', 23.25], ['Dec 16, 2021', 23.39], ['Dec 15, 2021', 23.46], ['Dec 14, 2021', 23.34], ['Dec 13, 2021', 23.01], ['Dec 10, 2021', 23.08], ['Dec 09, 2021', 22.69], ['Dec 08, 2021', 23.05], ['Dec 07, 2021', 22.53], ['Dec 06, 2021', 22.3], ['Dec 03, 2021', 22.5], ['Dec 02, 2021', 22.22], ['Dec 01, 2021', 21.71]]
PETR4_M0=[['Sep 30, 2021', 27.23], ['Sep 29, 2021', 27.39], ['Sep 28, 2021', 26.96], ['Sep 27, 2021', 27.14], ['Sep 24, 2021', 26.9], ['Sep 23, 2021', 26.84], ['Sep 22, 2021', 25.85], ['Sep 21, 2021', 25.21], ['Sep 20, 2021', 24.65], ['Sep 17, 2021', 24.93], ['Sep 16, 2021', 26.1], ['Sep 15, 2021', 26.33], ['Sep 14, 2021', 25.88], ['Sep 13, 2021', 26.23], ['Sep 10, 2021', 25.34], ['Sep 09, 2021', 25.5], ['Sep 08, 2021', 24.97], ['Sep 06, 2021', 26.46], ['Sep 03, 2021', 26.33], ['Sep 02, 2021', 26.6], ['Sep 01, 2021', 27.04]]
PETR4_M1_OPEN=['Oct 01, 2021', 27.12]
PETR4_M1=[['Oct 29, 2021', 27.25], ['Oct 28, 2021', 28.96], ['Oct 27, 2021', 28.69], ['Oct 26, 2021', 28.76], ['Oct 25, 2021', 29.04], ['Oct 22, 2021', 27.18], ['Oct 21, 2021', 27.45], ['Oct 20, 2021', 28.41], ['Oct 19, 2021', 28.01], ['Oct 18, 2021', 29.45], ['Oct 15, 2021', 29.6], ['Oct 14, 2021', 29.68], ['Oct 13, 2021', 29.63], ['Oct 11, 2021', 29.32], ['Oct 08, 2021', 29.12], ['Oct 07, 2021', 28.6], ['Oct 06, 2021', 28.64], ['Oct 05, 2021', 29.42], ['Oct 04, 2021', 28.79], ['Oct 01, 2021', 28.0]]
PETR4_M2_OPEN=['Nov 01, 2021', 27.71]
PETR4_M2=[['Nov 30, 2021', 29.43], ['Nov 29, 2021', 29.47], ['Nov 26, 2021', 28.47], ['Nov 25, 2021', 29.62], ['Nov 24, 2021', 28.37], ['Nov 23, 2021', 27.8], ['Nov 22, 2021', 26.36], ['Nov 19, 2021', 26.1], ['Nov 18, 2021', 26.54], ['Nov 17, 2021', 26.58], ['Nov 16, 2021', 27.27], ['Nov 12, 2021', 26.99], ['Nov 11, 2021', 26.45], ['Nov 10, 2021', 26.43], ['Nov 09, 2021', 26.64], ['Nov 08, 2021', 26.12], ['Nov 05, 2021', 25.85], ['Nov 04, 2021', 26.0], ['Nov 03, 2021', 26.85], ['Nov 01, 2021', 28.0]]
PETR4_M3_OPEN=['Dec 01, 2021', 29.84]
PETR4_M3=[['Dec 30, 2021', 28.45], ['Dec 29, 2021', 28.54], ['Dec 28, 2021', 28.78], ['Dec 27, 2021', 28.75], ['Dec 23, 2021', 28.33], ['Dec 22, 2021', 28.16], ['Dec 21, 2021', 28.2], ['Dec 20, 2021', 28.16], ['Dec 17, 2021', 28.99], ['Dec 16, 2021', 29.69], ['Dec 15, 2021', 29.3], ['Dec 14, 2021', 29.12], ['Dec 13, 2021', 29.47], ['Dec 10, 2021', 29.65], ['Dec 09, 2021', 29.29], ['Dec 08, 2021', 29.35], ['Dec 07, 2021', 29.36], ['Dec 06, 2021', 28.89], ['Dec 03, 2021', 28.76], ['Dec 02, 2021', 28.36], ['Dec 01, 2021', 29.6]]
ROMI3_M0=[['Sep 30, 2021', 19.11], ['Sep 29, 2021', 19.01], ['Sep 28, 2021', 19.49], ['Sep 27, 2021', 20.83], ['Sep 24, 2021', 20.97], ['Sep 23, 2021', 20.76], ['Sep 22, 2021', 20.59], ['Sep 21, 2021', 19.99], ['Sep 20, 2021', 20.27], ['Sep 17, 2021', 21.2], ['Sep 16, 2021', 21.52], ['Sep 15, 2021', 21.99], ['Sep 14, 2021', 21.39], ['Sep 13, 2021', 21.24], ['Sep 10, 2021', 20.71], ['Sep 09, 2021', 20.93], ['Sep 08, 2021', 19.84], ['Sep 06, 2021', 20.7], ['Sep 03, 2021', 20.74], ['Sep 02, 2021', 20.3], ['Sep 01, 2021', 21.61]]
ROMI3_M1_OPEN=['Oct 01, 2021', 19.24]
ROMI3_M1=[['Oct 29, 2021', 16.33], ['Oct 28, 2021', 16.73], ['Oct 27, 2021', 18.37], ['Oct 26, 2021', 18.04], ['Oct 25, 2021', 19.25], ['Oct 22, 2021', 18.32], ['Oct 21, 2021', 18.82], ['Oct 20, 2021', 19.52], ['Oct 19, 2021', 18.94], ['Oct 18, 2021', 19.51], ['Oct 15, 2021', 19.2], ['Oct 14, 2021', 19.14], ['Oct 13, 2021', 19.4], ['Oct 11, 2021', 18.6], ['Oct 08, 2021', 18.73], ['Oct 07, 2021', 18.07], ['Oct 06, 2021', 18.29], ['Oct 05, 2021', 18.09], ['Oct 04, 2021', 18.56], ['Oct 01, 2021', 19.71]]
ROMI3_M2_OPEN=['Nov 01, 2021', 16.51]
ROMI3_M2=[['Nov 30, 2021', 15.69], ['Nov 29, 2021', 15.35], ['Nov 26, 2021', 16.2], ['Nov 25, 2021', 17.24], ['Nov 24, 2021', 15.54], ['Nov 23, 2021', 14.7], ['Nov 22, 2021', 14.97], ['Nov 19, 2021', 15.33], ['Nov 18, 2021', 14.65], ['Nov 17, 2021', 15.06], ['Nov 16, 2021', 15.35], ['Nov 12, 2021', 16.66], ['Nov 11, 2021', 17.27], ['Nov 10, 2021', 16.76], ['Nov 09, 2021', 16.64], ['Nov 08, 2021', 16.41], ['Nov 05, 2021', 16.85], ['Nov 04, 2021', 16.54], ['Nov 03, 2021', 16.91], ['Nov 01, 2021', 17.03]]
ROMI3_M3_OPEN=['Dec 01, 2021', 15.85]
ROMI3_M3=[['Dec 30, 2021', 18.41], ['Dec 29, 2021', 17.09], ['Dec 28, 2021', 17.98], ['Dec 27, 2021', 17.72], ['Dec 23, 2021', 18.64], ['Dec 22, 2021', 18.06], ['Dec 21, 2021', 17.46], ['Dec 20, 2021', 17.87], ['Dec 17, 2021', 18.69], ['Dec 16, 2021', 19.01], ['Dec 15, 2021', 19.1], ['Dec 14, 2021', 18.52], ['Dec 13, 2021', 18.8], ['Dec 10, 2021', 18.36], ['Dec 09, 2021', 17.57], ['Dec 08, 2021', 18.29], ['Dec 07, 2021', 16.35], ['Dec 06, 2021', 16.18], ['Dec 03, 2021', 15.24], ['Dec 02, 2021', 14.79], ['Dec 01, 2021', 14.7]]
VALE3_M0=[['Sep 30, 2021', 76.24], ['Sep 29, 2021', 75.8], ['Sep 28, 2021', 74.85], ['Sep 27, 2021', 78.8], ['Sep 24, 2021', 77.69], ['Sep 23, 2021', 78.91], ['Sep 22, 2021', 78.91], ['Sep 21, 2021', 76.2], ['Sep 20, 2021', 75.47], ['Sep 17, 2021', 78.04], ['Sep 16, 2021', 79.66], ['Sep 15, 2021', 83.11], ['Sep 14, 2021', 85.24], ['Sep 13, 2021', 85.84], ['Sep 10, 2021', 85.89], ['Sep 09, 2021', 85.79], ['Sep 08, 2021', 86.1], ['Sep 06, 2021', 87.93], ['Sep 03, 2021', 89.33], ['Sep 02, 2021', 89.27], ['Sep 01, 2021', 89.55]]
VALE3_M1_OPEN=['Oct 01, 2021', 76.75]
VALE3_M1=[['Oct 29, 2021', 71.61], ['Oct 28, 2021', 73.7], ['Oct 27, 2021', 74.45], ['Oct 26, 2021', 76.18], ['Oct 25, 2021', 77.0], ['Oct 22, 2021', 76.08], ['Oct 21, 2021', 75.16], ['Oct 20, 2021', 76.41], ['Oct 19, 2021', 79.0], ['Oct 18, 2021', 79.92], ['Oct 15, 2021', 80.68], ['Oct 14, 2021', 79.2], ['Oct 13, 2021', 79.2], ['Oct 11, 2021', 81.62], ['Oct 08, 2021', 79.85], ['Oct 07, 2021', 79.36], ['Oct 06, 2021', 77.06], ['Oct 05, 2021', 74.95], ['Oct 04, 2021', 75.49], ['Oct 01, 2021', 76.2]]
VALE3_M2_OPEN=['Nov 01, 2021', 72.0]
VALE3_M2=[['Nov 30, 2021', 69.95], ['Nov 29, 2021', 69.5], ['Nov 26, 2021', 68.64], ['Nov 25, 2021', 70.5], ['Nov 24, 2021', 70.98], ['Nov 23, 2021', 69.37], ['Nov 22, 2021', 67.59], ['Nov 19, 2021', 64.03], ['Nov 18, 2021', 62.33], ['Nov 17, 2021', 65.0], ['Nov 16, 2021', 66.33], ['Nov 12, 2021', 68.3], ['Nov 11, 2021', 68.01], ['Nov 10, 2021', 65.69], ['Nov 09, 2021', 65.94], ['Nov 08, 2021', 67.6], ['Nov 05, 2021', 64.11], ['Nov 04, 2021', 66.07], ['Nov 03, 2021', 66.83], ['Nov 01, 2021', 72.32]]
VALE3_M3_OPEN=['Dec 01, 2021', 71.3]
VALE3_M3=[['Dec 30, 2021', 77.96], ['Dec 29, 2021', 77.25], ['Dec 28, 2021', 76.8], ['Dec 27, 2021', 78.95], ['Dec 23, 2021', 79.15], ['Dec 22, 2021', 79.92], ['Dec 21, 2021', 80.34], ['Dec 20, 2021', 78.28], ['Dec 17, 2021', 79.17], ['Dec 16, 2021', 80.44], ['Dec 15, 2021', 77.41], ['Dec 14, 2021', 77.85], ['Dec 13, 2021', 77.86], ['Dec 10, 2021', 75.65], ['Dec 09, 2021', 75.18], ['Dec 08, 2021', 75.76], ['Dec 07, 2021', 76.33], ['Dec 06, 2021', 75.77], ['Dec 03, 2021', 71.87], ['Dec 02, 2021', 73.49], ['Dec 01, 2021', 70.23]]

# WORKING WITH THE INITIAL PORTOFOLIO ##########################################################################################################

#Transforming the lists in dataframes to easier work
CAML3=pd.DataFrame(CAML3_M0, columns=['Date','Price'])
CPLE6=pd.DataFrame(CPLE6_M0, columns=['Date','Price'])
EMBR3=pd.DataFrame(EMBR3_M0, columns=['Date','Price'])
ITUB3=pd.DataFrame(ITUB3_M0, columns=['Date','Price'])
JHSF3=pd.DataFrame(JHSF3_M0, columns=['Date','Price'])
MRFG3=pd.DataFrame(MRFG3_M0, columns=['Date','Price'])
PCAR3=pd.DataFrame(PCAR3_M0, columns=['Date','Price'])
PETR4=pd.DataFrame(PETR4_M0, columns=['Date','Price'])
ROMI3=pd.DataFrame(ROMI3_M0, columns=['Date','Price'])
VALE3=pd.DataFrame(VALE3_M0, columns=['DATE','Price'])

#CACULATE THE STARDARD DEVIATION WITH STD BY LIB PANDAS

Deviation_CAML3=CAML3['Price'].std()
Deviation_CPLE6=CPLE6['Price'].std()
Deviation_EMBR3=EMBR3['Price'].std()
Deviation_ITUB3=ITUB3['Price'].std()
Deviation_JHSF3=JHSF3['Price'].std()
Deviation_MRFG3=MRFG3['Price'].std()
Deviation_PCAR3=PCAR3['Price'].std()
Deviation_PETR4=PETR4['Price'].std()
Deviation_ROMI3=ROMI3['Price'].std()
Deviation_VALE3=VALE3['Price'].std()

Deviation=[Deviation_CAML3,Deviation_CPLE6,Deviation_EMBR3,Deviation_ITUB3,Deviation_JHSF3,Deviation_MRFG3,Deviation_PCAR3,Deviation_PETR4,Deviation_ROMI3,Deviation_VALE3]

#To a correct pratice of deviation, in case of equal risk we need to compare deviation in percentage of the price, calculating (deviation/price of stock in day of rebalance
# In this case to initial portofolio we need to get the deviation of september and the open price of first day of october

CAML3_OPEN=CAML3_M1_OPEN[1]
CPLE6_OPEN=CPLE6_M1_OPEN[1]
EMBR3_OPEN=EMBR3_M1_OPEN[1]
ITUB3_OPEN=ITUB3_M1_OPEN[1]
JHSF3_OPEN=JHSF3_M1_OPEN[1]
MRFG3_OPEN=MRFG3_M1_OPEN[1]
PCAR3_OPEN=PCAR3_M1_OPEN[1]
PETR4_OPEN=PETR4_M1_OPEN[1]
ROMI3_OPEN=ROMI3_M1_OPEN[1]
VALE3_OPEN=VALE3_M1_OPEN[1]

OPEN_PRICES=[CAML3_OPEN,CPLE6_OPEN,EMBR3_OPEN,ITUB3_OPEN,JHSF3_OPEN,MRFG3_OPEN,PCAR3_OPEN,PETR4_OPEN,ROMI3_OPEN,VALE3_OPEN]
PRICE1=OPEN_PRICES

#We can distribute equal risk with deviation and deltas of portofolio, assigning one risk of 10% for each stock

risk=0.1
Delta_CAML3=risk/(Deviation_CAML3)
Delta_CPLE6=risk/(Deviation_CPLE6)
Delta_EMBR3=risk/(Deviation_EMBR3)
Delta_ITUB3=risk/(Deviation_ITUB3)
Delta_JHSF3=risk/(Deviation_JHSF3)
Delta_MRFG3=risk/(Deviation_MRFG3)
Delta_PCAR3=risk/(Deviation_PCAR3)
Delta_PETR4=risk/(Deviation_PETR4)
Delta_ROMI3=risk/(Deviation_ROMI3)
Delta_VALE3=risk/(Deviation_VALE3)

#to switch to delta in weight/percentage

Sum_Deltas=Delta_CAML3+Delta_CPLE6+Delta_EMBR3+Delta_ITUB3+Delta_JHSF3+Delta_MRFG3+Delta_PCAR3+Delta_PETR4+Delta_ROMI3+Delta_VALE3

Delta_CAML3=Delta_CAML3/Sum_Deltas
Delta_CPLE6=Delta_CPLE6/Sum_Deltas
Delta_EMBR3=Delta_EMBR3/Sum_Deltas
Delta_ITUB3=Delta_ITUB3/Sum_Deltas
Delta_JHSF3=Delta_JHSF3/Sum_Deltas
Delta_MRFG3=Delta_MRFG3/Sum_Deltas
Delta_PCAR3=Delta_PCAR3/Sum_Deltas
Delta_PETR4=Delta_PETR4/Sum_Deltas
Delta_ROMI3=Delta_ROMI3/Sum_Deltas
Delta_VALE3=Delta_VALE3/Sum_Deltas

Deltas=[Delta_CAML3,Delta_CPLE6,Delta_EMBR3,Delta_ITUB3,Delta_JHSF3,Delta_MRFG3,Delta_PCAR3,Delta_PETR4,Delta_ROMI3,Delta_VALE3]
DELTAS0=Deltas

#Assemble Report

Report_0=pd.DataFrame(({ 'Tickers': Tickers, 'Deltas': Deltas,'Deviation': Deviation,'Price 10/01/2021':OPEN_PRICES }))

# REBALANCE AFTER 1 MONTH######################################################################################################################

CAML3=pd.DataFrame(CAML3_M1, columns=['Date','Price'])
CPLE6=pd.DataFrame(CPLE6_M1, columns=['Date','Price'])
EMBR3=pd.DataFrame(EMBR3_M1, columns=['Date','Price'])
ITUB3=pd.DataFrame(ITUB3_M1, columns=['Date','Price'])
JHSF3=pd.DataFrame(JHSF3_M1, columns=['Date','Price'])
MRFG3=pd.DataFrame(MRFG3_M1, columns=['Date','Price'])
PCAR3=pd.DataFrame(PCAR3_M1, columns=['Date','Price'])
PETR4=pd.DataFrame(PETR4_M1, columns=['Date','Price'])
ROMI3=pd.DataFrame(ROMI3_M1, columns=['Date','Price'])
VALE3=pd.DataFrame(VALE3_M1, columns=['DATE','Price'])

#CACULATE THE STARDARD DEVIATION WITH STD BY LIB PANDAS

Deviation_CAML3=CAML3['Price'].std()
Deviation_CPLE6=CPLE6['Price'].std()
Deviation_EMBR3=EMBR3['Price'].std()
Deviation_ITUB3=ITUB3['Price'].std()
Deviation_JHSF3=JHSF3['Price'].std()
Deviation_MRFG3=MRFG3['Price'].std()
Deviation_PCAR3=PCAR3['Price'].std()
Deviation_PETR4=PETR4['Price'].std()
Deviation_ROMI3=ROMI3['Price'].std()
Deviation_VALE3=VALE3['Price'].std()

Deviation=[Deviation_CAML3,Deviation_CPLE6,Deviation_EMBR3,Deviation_ITUB3,Deviation_JHSF3,Deviation_MRFG3,Deviation_PCAR3,Deviation_PETR4,Deviation_ROMI3,Deviation_VALE3]

#To a correct pratice of deviation, in case of equal risk we need to compare deviation in percentage of the price, calculating (deviation/price of stock in day of rebalance
# In this case to first rebalance of portofolio we need to get the deviation of october and the open price of first day of november
CAML3_OPEN=CAML3_M2_OPEN[1]
CPLE6_OPEN=CPLE6_M2_OPEN[1]
EMBR3_OPEN=EMBR3_M2_OPEN[1]
ITUB3_OPEN=ITUB3_M2_OPEN[1]
JHSF3_OPEN=JHSF3_M2_OPEN[1]
MRFG3_OPEN=MRFG3_M2_OPEN[1]
PCAR3_OPEN=PCAR3_M2_OPEN[1]
PETR4_OPEN=PETR4_M2_OPEN[1]
ROMI3_OPEN=ROMI3_M2_OPEN[1]
VALE3_OPEN=VALE3_M2_OPEN[1]

OPEN_PRICES=[CAML3_OPEN,CPLE6_OPEN,EMBR3_OPEN,ITUB3_OPEN,JHSF3_OPEN,MRFG3_OPEN,PCAR3_OPEN,PETR4_OPEN,ROMI3_OPEN,VALE3_OPEN]
PRICE2=OPEN_PRICES

#We can distribute equal risk with deviation and deltas of portofolio, assigning one risk of 10% for each stock

risk=0.1
Delta_CAML3=risk/(Deviation_CAML3)
Delta_CPLE6=risk/(Deviation_CPLE6)
Delta_EMBR3=risk/(Deviation_EMBR3)
Delta_ITUB3=risk/(Deviation_ITUB3)
Delta_JHSF3=risk/(Deviation_JHSF3)
Delta_MRFG3=risk/(Deviation_MRFG3)
Delta_PCAR3=risk/(Deviation_PCAR3)
Delta_PETR4=risk/(Deviation_PETR4)
Delta_ROMI3=risk/(Deviation_ROMI3)
Delta_VALE3=risk/(Deviation_VALE3)

#to switch to delta in weight/percentage

Sum_Deltas=Delta_CAML3+Delta_CPLE6+Delta_EMBR3+Delta_ITUB3+Delta_JHSF3+Delta_MRFG3+Delta_PCAR3+Delta_PETR4+Delta_ROMI3+Delta_VALE3

Delta_CAML3=Delta_CAML3/Sum_Deltas
Delta_CPLE6=Delta_CPLE6/Sum_Deltas
Delta_EMBR3=Delta_EMBR3/Sum_Deltas
Delta_ITUB3=Delta_ITUB3/Sum_Deltas
Delta_JHSF3=Delta_JHSF3/Sum_Deltas
Delta_MRFG3=Delta_MRFG3/Sum_Deltas
Delta_PCAR3=Delta_PCAR3/Sum_Deltas
Delta_PETR4=Delta_PETR4/Sum_Deltas
Delta_ROMI3=Delta_ROMI3/Sum_Deltas
Delta_VALE3=Delta_VALE3/Sum_Deltas

Deltas=[Delta_CAML3,Delta_CPLE6,Delta_EMBR3,Delta_ITUB3,Delta_JHSF3,Delta_MRFG3,Delta_PCAR3,Delta_PETR4,Delta_ROMI3,Delta_VALE3]
DELTAS1=Deltas

#REPORT MONTH 1

Report_1=pd.DataFrame(({ 'Tickers': Tickers, 'Deltas': Deltas,'Deviation': Deviation,'Price 11/01/2021':OPEN_PRICES }))

# REBALANCE AFTER 2 MONTH ######################################################################################################################

CAML3=pd.DataFrame(CAML3_M2, columns=['Date','Price'])
CPLE6=pd.DataFrame(CPLE6_M2, columns=['Date','Price'])
EMBR3=pd.DataFrame(EMBR3_M2, columns=['Date','Price'])
ITUB3=pd.DataFrame(ITUB3_M2, columns=['Date','Price'])
JHSF3=pd.DataFrame(JHSF3_M2, columns=['Date','Price'])
MRFG3=pd.DataFrame(MRFG3_M2, columns=['Date','Price'])
PCAR3=pd.DataFrame(PCAR3_M2, columns=['Date','Price'])
PETR4=pd.DataFrame(PETR4_M2, columns=['Date','Price'])
ROMI3=pd.DataFrame(ROMI3_M2, columns=['Date','Price'])
VALE3=pd.DataFrame(VALE3_M2, columns=['DATE','Price'])

#CACULATE THE STARDARD DEVIATION WITH STD BY LIB PANDAS

Deviation_CAML3=CAML3['Price'].std()
Deviation_CPLE6=CPLE6['Price'].std()
Deviation_EMBR3=EMBR3['Price'].std()
Deviation_ITUB3=ITUB3['Price'].std()
Deviation_JHSF3=JHSF3['Price'].std()
Deviation_MRFG3=MRFG3['Price'].std()
Deviation_PCAR3=PCAR3['Price'].std()
Deviation_PETR4=PETR4['Price'].std()
Deviation_ROMI3=ROMI3['Price'].std()
Deviation_VALE3=VALE3['Price'].std()

Deviation=[Deviation_CAML3,Deviation_CPLE6,Deviation_EMBR3,Deviation_ITUB3,Deviation_JHSF3,Deviation_MRFG3,Deviation_PCAR3,Deviation_PETR4,Deviation_ROMI3,Deviation_VALE3]

#To a correct pratice of deviation, in case of equal risk we need to compare deviation in percentage of the price, calculating (deviation/price of stock in day of rebalance
# In this case to second rebalance of portofolio we need to get the deviation of october and the open price of first day of november

CAML3_OPEN=CAML3_M3_OPEN[1]
CPLE6_OPEN=CPLE6_M3_OPEN[1]
EMBR3_OPEN=EMBR3_M3_OPEN[1]
ITUB3_OPEN=ITUB3_M3_OPEN[1]
JHSF3_OPEN=JHSF3_M3_OPEN[1]
MRFG3_OPEN=MRFG3_M3_OPEN[1]
PCAR3_OPEN=PCAR3_M3_OPEN[1]
PETR4_OPEN=PETR4_M3_OPEN[1]
ROMI3_OPEN=ROMI3_M3_OPEN[1]
VALE3_OPEN=VALE3_M3_OPEN[1]

OPEN_PRICES=[CAML3_OPEN,CPLE6_OPEN,EMBR3_OPEN,ITUB3_OPEN,JHSF3_OPEN,MRFG3_OPEN,PCAR3_OPEN,PETR4_OPEN,ROMI3_OPEN,VALE3_OPEN]
PRICE3=OPEN_PRICES

#We can distribute equal risk with deviation and deltas of portofolio, assigning one risk of 10% for each stock

risk=0.1
Delta_CAML3=risk/(Deviation_CAML3)
Delta_CPLE6=risk/(Deviation_CPLE6)
Delta_EMBR3=risk/(Deviation_EMBR3)
Delta_ITUB3=risk/(Deviation_ITUB3)
Delta_JHSF3=risk/(Deviation_JHSF3)
Delta_MRFG3=risk/(Deviation_MRFG3)
Delta_PCAR3=risk/(Deviation_PCAR3)
Delta_PETR4=risk/(Deviation_PETR4)
Delta_ROMI3=risk/(Deviation_ROMI3)
Delta_VALE3=risk/(Deviation_VALE3)

#to switch to delta in weight/percentage

Sum_Deltas=Delta_CAML3+Delta_CPLE6+Delta_EMBR3+Delta_ITUB3+Delta_JHSF3+Delta_MRFG3+Delta_PCAR3+Delta_PETR4+Delta_ROMI3+Delta_VALE3

Delta_CAML3=Delta_CAML3/Sum_Deltas
Delta_CPLE6=Delta_CPLE6/Sum_Deltas
Delta_EMBR3=Delta_EMBR3/Sum_Deltas
Delta_ITUB3=Delta_ITUB3/Sum_Deltas
Delta_JHSF3=Delta_JHSF3/Sum_Deltas
Delta_MRFG3=Delta_MRFG3/Sum_Deltas
Delta_PCAR3=Delta_PCAR3/Sum_Deltas
Delta_PETR4=Delta_PETR4/Sum_Deltas
Delta_ROMI3=Delta_ROMI3/Sum_Deltas
Delta_VALE3=Delta_VALE3/Sum_Deltas

Deltas=[Delta_CAML3,Delta_CPLE6,Delta_EMBR3,Delta_ITUB3,Delta_JHSF3,Delta_MRFG3,Delta_PCAR3,Delta_PETR4,Delta_ROMI3,Delta_VALE3]
DELTAS2=Deltas

#REPORT MONTH 2

Report_2=pd.DataFrame(({ 'Tickers': Tickers, 'Deltas': Deltas,'Deviation': Deviation,'Price 12/01/2021':OPEN_PRICES}))

# REBALANCE AFTER 3 MONTH ######################################################################################################################
CAML3=pd.DataFrame(CAML3_M3, columns=['Date','Price'])
CPLE6=pd.DataFrame(CPLE6_M3, columns=['Date','Price'])
EMBR3=pd.DataFrame(EMBR3_M3, columns=['Date','Price'])
ITUB3=pd.DataFrame(ITUB3_M3, columns=['Date','Price'])
JHSF3=pd.DataFrame(JHSF3_M3, columns=['Date','Price'])
MRFG3=pd.DataFrame(MRFG3_M3, columns=['Date','Price'])
PCAR3=pd.DataFrame(PCAR3_M3, columns=['Date','Price'])
PETR4=pd.DataFrame(PETR4_M3, columns=['Date','Price'])
ROMI3=pd.DataFrame(ROMI3_M3, columns=['Date','Price'])
VALE3=pd.DataFrame(VALE3_M3, columns=['DATE','Price'])

#CACULATE THE STARDARD DEVIATION WITH STD BY LIB PANDAS

Deviation_CAML3=CAML3['Price'].std()
Deviation_CPLE6=CPLE6['Price'].std()
Deviation_EMBR3=EMBR3['Price'].std()
Deviation_ITUB3=ITUB3['Price'].std()
Deviation_JHSF3=JHSF3['Price'].std()
Deviation_MRFG3=MRFG3['Price'].std()
Deviation_PCAR3=PCAR3['Price'].std()
Deviation_PETR4=PETR4['Price'].std()
Deviation_ROMI3=ROMI3['Price'].std()
Deviation_VALE3=VALE3['Price'].std()

Deviation=[Deviation_CAML3,Deviation_CPLE6,Deviation_EMBR3,Deviation_ITUB3,Deviation_JHSF3,Deviation_MRFG3,Deviation_PCAR3,Deviation_PETR4,Deviation_ROMI3,Deviation_VALE3]

#To a correct pratice of deviation, in case of equal risk we need to compare deviation in percentage of the price, calculating (deviation/price of stock in day of rebalance
# In this case to first rebalance of portofolio we need to get the deviation of october and the open price of first day of november
CAML3_OPEN=CAML3_M3[0][1]
CPLE6_OPEN=CPLE6_M3[0][1]
EMBR3_OPEN=EMBR3_M3[0][1]
ITUB3_OPEN=ITUB3_M3[0][1]
JHSF3_OPEN=JHSF3_M3[0][1]
MRFG3_OPEN=MRFG3_M3[0][1]
PCAR3_OPEN=PCAR3_M3[0][1]
PETR4_OPEN=PETR4_M3[0][1]
ROMI3_OPEN=ROMI3_M3[0][1]
VALE3_OPEN=VALE3_M3[0][1]

OPEN_PRICES=[CAML3_OPEN,CPLE6_OPEN,EMBR3_OPEN,ITUB3_OPEN,JHSF3_OPEN,MRFG3_OPEN,PCAR3_OPEN,PETR4_OPEN,ROMI3_OPEN,VALE3_OPEN]
PRICE4=OPEN_PRICES

#We can distribute equal risk with deviation and deltas of portofolio, assigning one risk of 10% for each stock

risk=0.1
Delta_CAML3=risk/(Deviation_CAML3)
Delta_CPLE6=risk/(Deviation_CPLE6)
Delta_EMBR3=risk/(Deviation_EMBR3)
Delta_ITUB3=risk/(Deviation_ITUB3)
Delta_JHSF3=risk/(Deviation_JHSF3)
Delta_MRFG3=risk/(Deviation_MRFG3)
Delta_PCAR3=risk/(Deviation_PCAR3)
Delta_PETR4=risk/(Deviation_PETR4)
Delta_ROMI3=risk/(Deviation_ROMI3)
Delta_VALE3=risk/(Deviation_VALE3)

#to switch to delta in weight/percentage

Sum_Deltas=Delta_CAML3+Delta_CPLE6+Delta_EMBR3+Delta_ITUB3+Delta_JHSF3+Delta_MRFG3+Delta_PCAR3+Delta_PETR4+Delta_ROMI3+Delta_VALE3

Delta_CAML3=Delta_CAML3/Sum_Deltas
Delta_CPLE6=Delta_CPLE6/Sum_Deltas
Delta_EMBR3=Delta_EMBR3/Sum_Deltas
Delta_ITUB3=Delta_ITUB3/Sum_Deltas
Delta_JHSF3=Delta_JHSF3/Sum_Deltas
Delta_MRFG3=Delta_MRFG3/Sum_Deltas
Delta_PCAR3=Delta_PCAR3/Sum_Deltas
Delta_PETR4=Delta_PETR4/Sum_Deltas
Delta_ROMI3=Delta_ROMI3/Sum_Deltas
Delta_VALE3=Delta_VALE3/Sum_Deltas

Deltas=[Delta_CAML3,Delta_CPLE6,Delta_EMBR3,Delta_ITUB3,Delta_JHSF3,Delta_MRFG3,Delta_PCAR3,Delta_PETR4,Delta_ROMI3,Delta_VALE3]
DELTAS3=Deltas

# REPORT MONTH 3

Report_3=pd.DataFrame(({ 'Tickers': Tickers, 'Deltas': Deltas,'Deviation': Deviation,'Price 12/30/2021':OPEN_PRICES }))


print('Assamble Report''\n', Report_0.to_string(),'\n')
print('1st Report''\n',Report_1.to_string(),'\n')
print('2nd Report''\n',Report_2.to_string(),'\n')
print('3rd Report(Final)''\n',Report_3.to_string(),'\n')

#Calculating the performance in percentage

Performance_report=pd.DataFrame({ 'Tickers': Tickers,'Initial Deltas': DELTAS0,'PRICE 10/01/2021':PRICE1, 'PRICE 11/01/2021':PRICE2})

Performance_report['PERFORMANCE 1st Month'] = 100*Performance_report['Initial Deltas']*(Performance_report['PRICE 11/01/2021']-Performance_report['PRICE 10/01/2021'])/Performance_report['PRICE 10/01/2021']

Performance1=Performance_report['PERFORMANCE 1st Month'].sum()

Performance_report=pd.DataFrame({ 'Deltas after month 1': DELTAS1, 'PRICE 11/01/2021':PRICE2, 'PRICE 12/01/2021':PRICE3})

Performance_report['PERFORMANCE 2nd Month'] = 100*Performance_report['Deltas after month 1']*(Performance_report['PRICE 12/01/2021']-Performance_report['PRICE 11/01/2021'])/Performance_report['PRICE 11/01/2021']

Performance2=Performance_report['PERFORMANCE 2nd Month'].sum()

Performance_report=pd.DataFrame({'Deltas after month 2': DELTAS2, 'PRICE 12/01/2021':PRICE3, 'PRICE 12/30/2021':PRICE4})

Performance_report['PERFORMANCE 3nd Month'] = 100*Performance_report['Deltas after month 2']*(Performance_report['PRICE 12/30/2021']-Performance_report['PRICE 12/01/2021'])/Performance_report['PRICE 12/01/2021']

Performance3=Performance_report['PERFORMANCE 3nd Month'].sum()

Month=["October/2021","November/2021","December/2021"]
Performance=[Performance1,Performance2,Performance3]
Performance_report=pd.DataFrame({ 'Month': Month, 'Performance each month(%)':Performance})

Performance_in_3months=((100+Performance1)*(100+Performance2)*(100+Performance3)/(100*100))-100

print(Performance_report)

print('\nPerformance in 3 month:.%.2f' % Performance_in_3months, "%",'\n')

#Trades necessarys to rebalance


#FIRST WE NEED TO DEFINE THE ASSET(IN PERCENTAGE) BECAUSE THE WEIGHT OF EACH STOCK ARE IN DELTAS

Asset_in_Assamble=100
Asset_after_month1=100+Performance1
Asset_after_month2=(100+Performance2)*(Asset_after_month1/100)
Asset_after_month3=(100+Performance3)*(Asset_after_month2/100)


#month1

TRADES1=pd.DataFrame({'Tickers':Tickers,'Deltas in assamble':DELTAS0, 'Deltas 1st Rebalance':DELTAS1})

TRADES1['Percentage of postion increase/deacrease(%)']=Asset_in_Assamble*TRADES1['Deltas 1st Rebalance']-Asset_after_month1*TRADES1['Deltas in assamble']

print('Trades after month 1''\n',TRADES1.to_string(),'\n')

# #month2

TRADES2=pd.DataFrame({'Tickers':Tickers, 'Deltas 1st Rebalance':DELTAS1, 'Deltas 2nd Rebalance':DELTAS2})

TRADES2['Percentage of postion increase/deacrease(%)']=Asset_after_month1*TRADES2['Deltas 2nd Rebalance']-Asset_after_month2*TRADES2['Deltas 1st Rebalance']

print('Trades after month 2''\n',TRADES2.to_string(),'\n')

#month3

TRADES3=pd.DataFrame({'Deltas 2nd Rebalance':DELTAS2, 'Deltas 3rd Rebalance':DELTAS3})

TRADES3['Percentage of postion increase/deacrease(%)']=Asset_after_month2*TRADES3['Deltas 3rd Rebalance']-Asset_after_month3*TRADES3['Deltas 2nd Rebalance']

print('Trades after month 3''\n',TRADES3.to_string(),'\n')
