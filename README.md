# Spreadsheet Analysis
## 2012 AP Results

### Data set details
- Origin of my data set
    - The data set I selected are the 2012 AP Results from NYC high schools. The data included the DBN of the school, the school name, the number of AP test takers per school, the total number of AP exams taken per school, and the number of AP exams passed per school. It comes from NYC Open Data. 
        - [Link to data] (https://data.cityofnewyork.us/Education/2012-AP-Results/9ct9-prf9/data_preview)
    - The original file was CSV.
- Table of Raw Data
| DBN     | SCHOOL NAME | Num of AP Test Takers | Num of AP Total Exams Taken | Num of AP Exams Passed |
|---------|-------------|-----------------------|-----------------------------|------------------------|
| 01M292  | HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES       | s                      | s                           | s                      |
| 01M448  | UNIVERSITY NEIGHBORHOOD HIGH SCHOOL                          | 37                     | 53                          | 21                     |
| 01M450  | EAST SIDE COMMUNITY SCHOOL                                   | 12                     | 12                          | s                      |
| 01M458  | FORSYTH SATELLITE ACADEMY                                    | s                      | s                           | s                      |
| 01M509  | MARTA VALLE HIGH SCHOOL                                      | 14                     | 15                          | s                      |
| 01M515  | LOWER EAST SIDE PREPARATORY HIGH SCHOOL                       | 50                     | 60                          | 54                     |
| 01M539  | NEW EXPLORATIONS INTO SCIENCE, TECHNOLOGY AND MATH HIGH SCHOOL| 306                    | 587                         | 323                    |
| 01M650  | CASCADES HIGH SCHOOL                                         | s                      | s                           | s                      |
| 01M696  | BARD HIGH SCHOOL EARLY COLLEGE                               | s                      | s                           | s                      |
| 02M047  | 47 THE AMERICAN SIGN LANGUAGE AND ENGLISH SECONDARY SCHOOL  | s                      | s                           | s                      |
| 02M288  | FOOD AND FINANCE HIGH SCHOOL                                 | 41                     | 41                          | s                      |
| 02M294  | ESSEX STREET ACADEMY                                         | s                      | s                           | s                      |
| 02M296  | HIGH SCHOOL OF HOSPITALITY MANAGEMENT                        | s                      | s                           | s                      |
| 02M298  | PACE HIGH SCHOOL                                             | s                      | s                           | s                      |
| 02M300  | URBAN ASSEMBLY SCHOOL OF DESIGN AND CONSTRUCTION, THE        | 135                    | 135                         | 8                      |
| 02M303  | FACING HISTORY SCHOOL, THE                                   | 32                     | 32                          | s                      |
| 02M305  | URBAN ASSEMBLY ACADEMY OF GOVERNMENT AND LAW, THE            | 31                     | 40                          | 20                     |
| 02M308  | LOWER MANHATTAN ARTS ACADEMY                                 | 11                     | 11                          | s                      |
| 02M313  | JAMES BALDWIN SCHOOL, THE: A SCHOOL FOR EXPEDITIONARY LEARNING| s                      | s                           | s                      |

 Problems present in data
- Instead of '0,' the letter s appears. I needed to replace the 's' to ensure that correct calculations could be made during the analysis portion.
    ```python
            for row in reader:
            if dbn_index is not None:
                del row[dbn_index]
            row = [item.replace('s', '0') for item in row]

            ap_exams_taken = int(row[2]) 
            ap_exams_passed = int(row[3])  
- I removed the DBN column since it was unnecessary.
    ```python
            if 'DBN' in headers:
            dbn_index = headers.index('DBN')
            del headers[dbn_index]
        else:
            dbn_index = None

- I added a column titled Exam Pass rate to calculate the percentage for each school of exams passed/exams taken
    ```python
            ap_exams_taken = int(row[2]) 
            ap_exams_passed = int(row[3])  
            if ap_exams_taken != 0:
                pass_rate = round(ap_exams_passed / ap_exams_taken, 3)
            else:
                pass_rate = "N/A"
            row.append(pass_rate)

            writer.writerow(row)
- Links to the files
    - [Original Raw Data] (https://data.cityofnewyork.us/Education/2012-AP-Results/9ct9-prf9/data_preview)
    - [Munged Data] (data/clean_data.csv)
    - [Spreadsheet File] (data/analysis.xls)

### Analysis
- I first calculated the mean number of AP Test Takers, total exams taken, number of exams passed, and the exam passrate. I then rounded the numbers dealing with people to the whole number. Thus, across NYC schools in 2012, the average school had 67 AP exam takers, an average of 103 exams taken per school, an average of 55 exams passed, and an everage pass rate of 0.28. 
- I then calculated the min and max for each category. The minimum number of AP test takers, total exams taken, number of exams passed, and the exam passrate were all 0. The maximum number of AP test takers at a school in NYC in 2012 was 
2515, the highest number of total exams taken at a school was 4427, the highest number of AP exams passed was 3333, and the highest pass rate was 0.972
- The total number of AP test takers in NYC in 2012 was 32406, 49703 exams were taken, and 26660 exams were passed. 
- Insight: Given that the mean is 67 test takers and one school had 2515, the disparities in the number of people taking AP exams in 2012 in NYC are quite large. There is a large range in the success of these students as well since the average pass rate is 28%, but the highest passrate is 97.2%
- The formula =AVERAGEIF(B2:B479, ">67", C2:C479) calculates the average number of AP exams taken per school where the number of AP test takers is higher than 67 which is the mean. This calculation allows for a more focused analysis of the number of AP test takers since it mostly looks at schools with a higher number of exam testers and excludes 0s. The average calculated is 444.173 which is significantly higher than 67. 
- The formula =COUNTIF(E2:E479, ">=0.5") calculates the count of schools where the pass rate is greater than or equal to 0.5. By focusing on schools with pass rates above or equal to 0.5, the statistic identifies the number of schools that have achieved a certain level of success in their AP programs. The total count is 57.
- The formula =SUMIF(E2:E479, ">0.5", B2:B479) calculates the total number of AP test takers across all schools where the pass rate is greater than 0.5. This identifies how many students attend schools that are high achieving for AP exams. The number is 17626. 
- The formula =MAXIFS(C2:C479, E2:E479, "<0.5") calculates the maximum number of AP exams taken at a school where the pass rate is less than 0.5. The statistic highlights the maximum level of AP participation among schools where student success in AP exams may be lower. The highest number of participants is 1056 amongst this group which is more than half the school with the highest passrate. 
- Pivot Table
Sum of Num of AP Exams Passed
| SCHOOL NAME                                                          | Total |
|----------------------------------------------------------------------|-------|
| BROOKLYN TECHNICAL HIGH SCHOOL                                       | 3333  |
| BRONX HIGH SCHOOL OF SCIENCE                                         | 2986  |
| STUYVESANT HIGH SCHOOL                                               | 2608  |
| FIORELLO H. LAGUARDIA HIGH SCHOOL OF MUSIC & ART AND PERFORMING ARTS | 1177  |
| STATEN ISLAND TECHNICAL HIGH SCHOOL                                  | 977   |
| TOWNSEND HARRIS HIGH SCHOOL                                          | 937   |
| BENJAMIN N. CARDOZO HIGH SCHOOL                                      | 873   |
| FRANCIS LEWIS HIGH SCHOOL                                            | 712   |
| MIDWOOD HIGH SCHOOL                                                  | 706   |
| FOREST HILLS HIGH SCHOOL                                             | 629   |
| BAYSIDE HIGH SCHOOL                                                  | 493   |
| FORT HAMILTON HIGH SCHOOL                                            | 414   |
| EDWARD R. MURROW HIGH SCHOOL                                         | 406   |
| LEON M. GOLDSTEIN HIGH SCHOOL FOR THE SCIENCES                       | 398   |
| QUEENS HIGH SCHOOL FOR THE SCIENCES AT YORK COLLEGE                  | 345   |

The pivot table ranks schools by the number of Advanced Placement (AP) exams passed. This reveals which schools perform the best in regards to most AP exams passed. This allows for understanding on where schools may need to bolster their AP programs. It also reveals disparities within New York city schools, suggesting where additional resources—such as teaching staff, educational materials, or student support services—might be most effectively deployed. 

- ! [Screenshot of a scatterplot demonstrating the relation between total number of exams taken and total number of exams passed at each school] (data/chart.png)

The scatter plot illustrates the relationship between the total number of AP exams taken and the number of exams passed at each school. Each point on the plot represents a school, with its position indicating both the volume of exams undertaken and the success rate in terms of exams passed. This visualization can help in understanding how exam participation levels relate to achievement rates across the schools. If there's anything else you'd like to explore or any other questions, feel free to ask!