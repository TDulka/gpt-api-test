import openai

openai.api_key_path = './key'

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": """You are a graduate research assistant in economics. 
#         Your task is to annotate abstracts of economics papers. 
#         You will be presented with the text and label spans with braces following with the label in parenthesis, for example {this is a span}(label). 
#         Spans cannot overlap. Annotate the minimum span length necessary and split neighboring entities into multiple spans where needed. 
#         Possible labels are intervention, outcome, population and effect_size. You will also need to adhere to the following rules.       
# Rules:
# - An entity can span over one or to more consecutive tokens (words).
# - An entity cannot span across sentence boundaries
# - Try not to include determinators (such as the, a), or adjective pronouns (such as this, its, these, such) to the span
# - Annotate the minimum number of tokens such that the entity is still well defined
# - Label only the intervention that is examined in the study.
# - Label only outcomes related to the intervention, measured in the study. An outcome is the likely or achieved change and effects of an intervention. 
# - We annotate program names and acronyms of interventions as interventions, e.g. Start-and-Improve Your Business (SIYB) Program, No Child Left Behind, Progresa
# - Include generic terms in the intervention span when they describe the entity, e.g. program, courses, lectures. For example in the sentence “We used a randomized experiment to measure the impact of business training courses” the generic term courses should also be part of the intervention span (business training courses). 
# - Do not include delivery details or attributes of the interventions. For example, in the sentence “Carrying of firearms was banned on weekends after paydays, on holidays and on election days.” the intervention span should be Carrying of firearms was banned excluding the details on which day the ban took place.
# - Include in the span generic references such as the word “effects” when they are next to an outcome.
# - The population, sometimes referred to as population target, is the group of people on which the intervention is implemented or in which the outcome is measured.
# - We annotate all mentions of the population in the text with the label population. This includes mentions of subgroups of the population where the intervention was applied or on whom an outcome was measured.
# - If the text mentions a control group that had a different population and did not receive an intervention, we do not annotate that. We are only interested in the populations that received an intervention.
# - We do not annotate generic references such as the word “population” with the population tag.
# - If a population is mentioned next to an outcome, for example “children’s weight-for-height score”, we label “children” separately as population and “weight-for-height score” as outcome.
# - Do not label Unit of interventions, e.g. individuals, households, villages as population 
# - Do not label Treated group, e.g. impregnated chaddar users (impregnated chaddar is the intervention; user is a generic term and not labeled) as population
# - Do not label Geographical names such as countries, regions or cities, e.g. rural Bangladesh (rural is the population; Bangladesh is the country and should not be included in the span)
# - Effect sizes are the mentions of quantitative measures of the magnitude of the intervention’s effect in an outcome.
# - Effect sizes are the specific numeric measure, not general discussions of effects.
# - Whenever possible, the effect size span should include not only the numeric measure but also the unit of measure, as long as this is not part of an outcome span.
# - We tag all the mentions of effect sizes, including mentions for different treatment groups, subgroups, control groups, or about the difference between treatment and control groups.
# - Do not include in the span words indicating the direction of the effect size (example: increment, decrease, increase). 
# - Statistical measures such as t-stats, p-values, or confidence intervals should not be considered effect sizes.
# - Odds ratios and incidence rate ratios should be considered effect sizes
# """},
#         {
#             "role": "user", 
#             "content": "Background: Inappropriate nutrition knowledge and feeding practices of caregivers are among several important causes of persistent malnutrition problems in young children. Thus, it is essential to provide caregivers with the necessary knowledge to help them modify their feeding practices. Objective: To examine the effectiveness of two different nutrition education methods, weekly intensive nutrition education (INE) and monthly nonintensive nutrition education (NNE), designed for caregivers of mildly wasted children (weight-for-height z-score ≥ -1.5 to < -1) aged ≥ 6 to < 60 months on Nias Island, Indonesia. Methods: To assess the impact of the two different nutrition education approaches on nutrition knowledge and practice of caregivers with their children, respondents were assigned to receive either weekly INE (n=114) or monthly NNE (n=96). The knowledge and practice levels of the mothers in each group were assessed and compared using a pretested validated questionnaire at admission and after the intervention period. Results: At admission, the knowledge and practice levels of caregivers in both groups were not statistically significantly different. After participating in the nutrition education program, the percentage of correct answers on nutrition knowledge and practice in the INE group was significantly higher than that in the NNE group. Significant improvement in knowledge and practice scores was observed in the INE group after the intervention (p < 0.001), whereas only a significant improvement in knowledge was found in the NNE group (p < .05). Conclusions: In comparison with NNE, the INE approach was significantly better in bringing about a positive change in knowledge and practice of caregivers of mildly wasted children in the study area."},
#         {
#             "role": "assistant",
#             "content": "Background: Inappropriate {nutrition knowledge}(outcome) and {feeding practices}(outcome) of {caregivers}(population) are among several important causes of persistent {malnutrition problems}(outcome) in {young children}(population). Thus, it is essential to provide {caregivers}(population) with the necessary {knowledge}(intervention) to help them modify their {feeding practices}(outcome). Objective: To examine the effectiveness of two different {nutrition education methods}(intervention), {weekly intensive nutrition education (INE)}(intervention) and {monthly nonintensive nutrition education (NNE)}(intervention), designed for {caregivers of mildly wasted children}(population) ({weight-for-height}(outcome) z-score ≥ -1.5 to < -1) {aged ≥ 6 to < 60 months}(population) on Nias Island, Indonesia. Methods: To assess the impact of the two different {nutrition education}(intervention) approaches on {nutrition knowledge}(outcome) and {practice}(outcome) of {caregivers}(population) with their {children}(population), respondents were assigned to receive either weekly {INE}(intervention) (n=114) or monthly {NNE}(intervention) (n=96). The {knowledge}(outcome) and {practice}(outcome) levels of the {mothers}(population) in each group were assessed and compared using a pretested validated questionnaire at admission and after the intervention period. Results: At admission, the {knowledge}(outcome) and {practice}(outcome) levels of {caregivers}(population) in both groups were not statistically significantly different. After participating in the {nutrition education program}(intervention), the percentage of correct answers on {nutrition knowledge}(outcome) and {practice}(outcome) in the {INE}(intervention) group was significantly higher than that in the {NNE}(intervention) group. Significant improvement in {knowledge}(outcome) and {practice}(outcome) scores was observed in the {INE}(intervention) group after the intervention (p < 0.001), whereas only a significant improvement in {knowledge}(outcome) was found in the {NNE}(intervention) group (p < .05). Conclusions: In comparison with {NNE}(intervention), the {INE}(intervention) approach was significantly better in bringing about a positive change in {knowledge}(outcome) and {practice}(outcome) of {caregivers of mildly wasted children}(population) in the study area."
#         },
#         {
#             "role": "user",
#             "content": "About 10% of primary school students in developing countries have poor vision, but very few of them wear glasses. Almost no research examines the impact of poor vision on school performance, and simple OLS estimates could be biased because studying harder may adversely affects one’s vision. This paper presents results from a randomized trial in Western China that offered free eyeglasses to rural primary school students. Our preferred estimates, which exclude township pairs for which students in the control township were mistakenly provided eyeglasses, indicate that wearing eyeglasses for one academic year increased the average test scores of students with poor vision by 0.16 to 0.22 standard deviations, equivalent to 0.3 to 0.5 additional years of schooling. These estimates are averages across the two counties where the intervention was conducted. We also find that the benefits are greater for under-performing students. A simple cost-benefit analysis suggests very high economic returns to wearing eyeglasses, raising the question of why such investments are not made by most families. We find that girls are more likely to refuse free eyeglasses, and that parental lack of awareness of vision problems, mothers’ education, and economic factors (expenditures per capita and price) significantly affect whether children wear eyeglasses in the absence of the intervention."
#         },
#         {
#             "role": "assistant",
#             "content": "About 10% of {primary school students}(population) in developing countries have {poor vision}(outcome), but very few of them wear {glasses}(intervention). Almost no research examines the impact of {poor vision}(outcome) on {school performance}(outcome), and simple OLS estimates could be biased because studying harder may adversely affects one’s {vision}(outcome). This paper presents results from a randomized trial in Western China that offered {free eyeglasses}(intervention) to {rural primary school students}(population). Our preferred estimates, which exclude township pairs for which {students}(population) in the control township were mistakenly provided eyeglasses, indicate that wearing {eyeglasses}(intervention) for one academic year increased the average {test scores}(outcome) of {students with poor vision}(population) by {0.16 to 0.22 standard deviations}(effect_size), equivalent to {0.3 to 0.5 additional years of schooling}(effect_size). These estimates are averages across the two counties where the intervention was conducted. We also find that the benefits are greater for {under-performing students}(population). A simple cost-benefit analysis suggests very high {economic returns}(outcome) to wearing {eyeglasses}(intervention), raising the question of why such investments are not made by most families. We find that {girls}(population) are more likely to refuse free eyeglasses, and that parental lack of awareness of vision problems, {mothers}(population)' education, and economic factors (expenditures per capita and price) significantly affect whether {children}(population) {wear eyeglasses}(outcome) in the absence of the intervention."
#         },
#         {
#             "role": "user",
#             "content": "We use a randomized experiment and a structural model to test whether monitoring and financial incentives can reduce teacher absence and increase learning in India. In treatment schools, teachers’ attendance was monitored daily using cameras, and their salaries were made a nonlinear function of attendance. Teacher absenteeism in the treatment group fell by 21 percentage points relative to the control group, and the children’s test scores increased by 0.17 standard deviations. We estimate a structural dynamic labor supply model and find that teachers respond strongly to financial incentives. Our model is used to compute cost-minimizing compensation policies."
#         },
#         {
#             "role": "assistant",
#             "content": "We use a randomized experiment and a structural model to test whether {monitoring}(intervention) and {financial incentives}(intervention) can reduce {teacher}(population) {absence}(outcome) and increase {learning}(outcome) in India. In treatment schools, {teachers’}(population) {attendance}(outcome) was monitored daily using cameras, and their {salaries were made a nonlinear function of attendance}(intervention). {Teacher}(population) {absenteeism}(outcome) in the treatment group fell by {21 percentage points}(effect_size) relative to the control group, and the {children’s}(population) {test scores}(outcome) increased by {0.17 standard deviations}(effect_size). We estimate a structural dynamic labor supply model and find that {teachers}(population) respond strongly to {financial incentives}(intervention). Our model is used to compute cost-minimizing compensation policies."
#         },
#         {
#             "role": "user",
#             "content": "Bullying has been described as one of the most tractable risk factors for poor mental health and educational outcomes, yet there is a lack of evidence-based interventions for use in low and middle-income settings. We aimed to develop and assess the feasibility of an adolescent-led school intervention for reducing bullying among adolescents in Indonesian secondary schools. The intervention was developed in iterative stages: identifying promising interventions for the local context; formative participatory action research to contextualize proposed content and delivery; and finally two pilot studies to assess feasibility and acceptability in South Sulawesi and Central Java. The resulting intervention combines two key elements: 1) a student-driven design to influence students pro-social norms and behavior, and 2) a teacher-training component designed to enhance teacher’s knowledge and self-efficacy for using positive discipline practices. In the first pilot study, we collected data from 2,075 students in a waitlist-controlled trial in four schools in South Sulawesi. The pilot study demonstrated good feasibility and acceptability of the intervention. We found reductions in bullying victimization and perpetration when using the Forms of Bullying Scale. In the second pilot study, we conducted a randomised waitlist controlled trial in eight schools in Central Java, involving a total of 5,517 students. The feasibility and acceptability were good. The quantitative findings were more mixed, with bullying perpetration and victimization increasing in both control and intervention schools. We have designed an intervention that is acceptable to various stakeholders, feasible to deliver, is designed to be scalable, and has a clear theory of change in which targeting adolescent social norms drives behavioral change. We observed mixed findings across different sites, indicating that further adaptation to context may be needed. A full-randomized controlled trial is required to examine effectiveness and cost-effectiveness of the program."
#         }
#     ],
#     temperature = 1
# )

messages = [
  {"role": "system", "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English."},
  {"role": "system", "name":"example_user", "content": "New synergies will help drive top-line growth."},
  {"role": "system", "name": "example_assistant", "content": "Things working well together will increase revenue."},
  {"role": "system", "name":"example_user", "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage."},
  {"role": "system", "name": "example_assistant", "content": "Let's talk later when we're less busy about how to do better."},
  {"role": "user", "content": "This late pivot means we don't have time to boil the ocean for the client deliverable."},
]

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = messages
)

print(response)