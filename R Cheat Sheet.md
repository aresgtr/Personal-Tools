# R Cheat Sheet

## Basic Operations

Check documentation

```r
?load()
```

Assign Value to an Object

```r
result <- 5 * (10-4) / 10 + 2 - 5.5
```
Math operations

```r
sqrt(10)
pi
3*4^2
(3*4)^2
```

Vectors (List)

```r
world.pop <- c(2525779, 3026003, 3691173, 4449049, 5320817, 6127700, 6916183)
```

Two splitted vectors can be combined

```r
pop.first <- c(2525779, 3026003, 3691173)
pop.second <- c(4449049, 5320817, 6127700, 6916183)
pop.all <- c(pop.first, pop.second)
pop.all
```

```r
# 第三位
world.pop[3]

# 第一，四，六位 (R start from index 1，没有第0位)
world.pop[c(1,4,6)]
```

把`world.pop`这个`vector`里面的所有数除以**1000**

```r
pop.million <- world.pop / 1000 
```

Functions for vectors

```r
length(world.pop)

min(world.pop)

max(world.pop)

range(world.pop)

mean(world.pop)

sum(world.pop) / length(world.pop)
```

Loop
```r
> 1:10
 [1]  1  2  3  4  5  6  7  8  9 10

> rep(1:3, each = 4)
 [1] 1 1 1 1 2 2 2 2 3 3 3 3

> rep(1:3, times = 4) #cf. "each"
 [1] 1 2 3 1 2 3 1 2 3 1 2 3

> seq(from = 1, to = 100, by = 5)
 [1]  1  6 11 16 21 26 31 36 41 46 51 56 61 66 71 76 81 86 91 96
```

## Data Files

```r
load("C:/Users/zyche/Desktop/T/wvs7.RData")

# Set working directory
setwd("C:/Users/zyche/Desktop/T")
getwd()

#这种方法直接把 object name 设成 wvs7
load("wvs7.RData")

data2 <- read.csv("wvs7.csv")
```

### Explore data

```r
# returns the numbers of observations and variables
dim(data2)
nrow(data2)
ncol(data2)

# returns the variable names
names(data2)
colnames(data2)

# returns the variable names
names(data2)
colnames(data2)

class(data2)
class(wvs7$doi) 
class(wvs7$w_weight)

# print the data structure
# (每一列的 datatype 都会显示出来，还会list那一列的前几个data)
str(data2)
str(data2$w_weight)

# count 每一个 unique value 有多少个
table(wvs7$q92)

# Head / Tails
head(wvs7)
tail(wvs7)
```

Summary Statistics

```r
# 每一列的都搞出来
summary(data2)

# 单独看一列
summary(data2$w_weight)

# 单独看几列
summary(data2[c("w_weight")])
```

Save data

```r
## save csv data
write.csv(data2, file = "data3.csv")

write.csv(x=mydf, 
          file="basicinfo_xpt.csv",
          row.names = F) # Row names excluded

## save R data
save(data2,file="data3.RData")

save(wvs7_csv, wvs7_xlsx, file="D:/Dropbox/Teaching/QDA/Courses/SOSC2400_2021F/^Shared/Classes/W3/R/wvs7_2.RData")
```

土法自制 Data Frame

```r
var1 <- c("A","B","C","D","E")         # string
var2 <- c(21,34,56,54,32)              # numeric
var3 <- c(TRUE,FALSE,TRUE,FALSE,FALSE) # logical

mydata1 <- data.frame(
  name1 = c("A","B","C","D","E"),
  name2 = c(21,34,56,54,32),
  name3 = c(TRUE,FALSE,TRUE,FALSE,FALSE)
)

dim(mydata1)
class(mydata1)
```

Correlation

```r
# FYI 里面的例子
cor(USArrests$Murder, USArrests$Assault)
```

## Packages

```r
install.packages("readxl") # Only need to be carried out once

# Load package (二选一)
library(readxl)
require(readxl)

wvs7_xlsx<-read_excel("wvs7.xlsx")

wvs7_xlsx<-read_excel("D:/Dropbox/Teaching/QDA/Courses/SOSC2400_2021F/^Shared/Classes/W3/R/wvs7.xlsx", col_names = TRUE) #Again, watch out for missing values

save(wvs7_csv, wvs7_xlsx, file="D:/Dropbox/Teaching/QDA/Courses/SOSC2400_2021F/^Shared/Classes/W3/R/wvs7_2.RData")
```

To see which packages are currently attached. You can also check in the **Packages** window

```r
sessionInfo()
```

## Plots

### Bar Plot

```r
barplot(table(wvs7$ms))
```

<img src="R_Cheat_Sheet/barplot_before" width="400">

```r
# Modified barplot
barplot(sort(table(wvs7$ms), decreasing=T), 
        main="Marital Status, WVS 7", 
        ylab="Count", ylim=c(0,1200), 
        names.arg=c("Married", "Living together as married", "Divorced", "Separated", "Widowed", "Single"),
        las=2
        ) 
```

<img src="R_Cheat_Sheet/barplot_after" width="400">

---

### Histogram

```r
hist(wvs7$age)
```
<img src="R_Cheat_Sheet/histplot1" width="400">

```r
# prob instead of count for y axis
hist(wvs7$age, prob = TRUE)
```

<img src="R_Cheat_Sheet/histplot2" width="400">

```r
hist(wvs7$age,
     probability=TRUE,  
     breaks = 15, # specify #intervals
     xlab = "Age",
     main = "Distribution of Age (WVS, Wave 7)")

lines(density(wvs7$age, na.rm = T))  # FYI
```

<img src="R_Cheat_Sheet/histplot3" width="400">

---

### Boxplot

```r
boxplot(wvs7$age)
```
<img src="R_Cheat_Sheet/boxplot" width="400">
