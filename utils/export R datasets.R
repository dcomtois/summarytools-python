library(summarytools)
names(tabagisme) <- gsub("\\.", "_", names(tabagisme))
write.table(tabagisme, file = "./data/tabagisme.csv", row.names = FALSE, na = "")

names(tobacco) <- gsub("\\.", "_", names(tobacco))
write.csv(tobacco, file = "./data/tobacco.csv", row.names = FALSE, na = "")

names(examens) <- gsub("\\.", "_", names(examens))
write.csv(examens, file = "./data/examsen.csv", row.names = FALSE, na = "")

names(exams) <- gsub("\\.", "_", names(exams))
write.csv(exams, file = "./data/exams.csv", row.names = FALSE, na = "")
