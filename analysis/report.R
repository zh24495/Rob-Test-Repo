library('tidyverse')

df_input <- read_csv(
  here::here("output", "dataset.csv.gz"),
)

plot_age <- ggplot(data=df_input, aes(df_input$number_of_medications)) + geom_histogram()

ggsave(
  plot= plot_age,
  filename="report.png", path=here::here("output"),
)