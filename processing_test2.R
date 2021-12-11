library(RGPR)
setwd("~")
setwd("Northeastern Docs/capstone/")
#print(paste('Reading from file: ', infile))
x <- readGPR(dsn = "2014_04_25_frenke/rawGPR/LINE04.DT1")
#x <- readGPR(dsn = "yyline3.DT1")

#x <- frenkeLine00 

print('DC shift')
x3 <- dcshift(x, u = 1:110)
print('time 0')
x3 <- estimateTime0(x3, w = 20, method = "coppens", thr = 0.05, FUN = mean)
x3 <- time0Cor(x3, method = "pchip")
print('dewow')
x3 <- dewow(x3, type = "runmed", w = 50)     # dewowing:
x3 <- fFilter(x3, f = c(200,300), type = "low")
x3 <- gainSEC(x3, a = 0.003, t0 = 50)

print(paste('Writing to file: ', outfile))
plot(x3)
plot(x)
writeGPR(x3, fPath = "procOut1", type = "ASCII", overwrite=TRUE)
x <- readGPR(dsn = "procOut1.txt") 

plot(x)