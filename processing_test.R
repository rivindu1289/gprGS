#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

#if (length(args)==2) {
#    infile = args[1]
#    outfile = args[2]
#} else {
#    stop("Input and output file need to be specified", call.=FALSE)
#}

setwd("~")
setwd("Northeastern Docs/capstone/")

library(RGPR)
# print("hello")

x <- readGPR(dsn = "yyline3.txt")
plot(x)

# plot the first 110 samples of the 15th trace of the GPR profile
plot(x[1:110, 15])
plot(x[, 15])  # plot the 15th trace of the GPR-line
# add a green horizontal line
abline(h = mean(x[1:110, 15]), col = "green")
x1 <- dcshift(x, u = 1:110)
plot(x1)
x2 <- estimateTime0(x1, w = 20, method = "coppens", thr = 0.05, FUN = mean)
plot(x2, pngName="test")


x3 <- dewow(x2, type = "Gaussian", w = 5)     # dewowing:
x3 <- fFilter(x3, f = c(200,300), type = "low")
x3 <- gainSEC(x3, a = 0.003, t0 = 50)
plot(x3)
writeGPR(x3, fPath = outfile, type = "xta", overwrite=TRUE)
plot(x3[1:500,1:75])  
plot(x3-x2)                                   # plot the result

# plot(x2[,15], col = "blue")      # before dewowing
# lines(x3[,15], col = "red")      # after dewowing
# plot(x3[,15])
# plot(x3[,30])
plot(x3[,13] - x3[,15])