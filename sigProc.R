#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

if (length(args)==2) {
    infile = args[1]
    outfile = args[2]
} else {
    stop("Input and output file need to be specified\nUsage: Rscript sigProc.R [inputFile] [outputFile]", call.=FALSE)
}

library(RGPR)
print(paste('Reading from file: ', infile))
x <- readGPR(dsn = infile) 

print('DC shift')
x1 <- dcshift(x, u = 1:110)
print('time 0')
x2 <- estimateTime0(x1, w = 20, method = "coppens", thr = 0.05, FUN = mean)
x2 <- time0Cor(x2, method = "pchip")
print('dewow')
x3 <- dewow(x2, type = "runmed", w = 50)
print('fFilter')
x3 <- fFilter(x3, f = c(200,300), type = "low")

print(paste('Writing to file: ', outfile))
writeGPR(x3, fPath = outfile, type = "ASCII", overwrite=TRUE)