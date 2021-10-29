# Deviency Score
<h1 align = "center">Description</h1>
<hr />

<p>
A simple bot created with using Reddit's PRAW library that returns a table of a user's illicit engagements. It also provides a score that denotes how willing a user is to engage with unscroupulous content compared to a random sample of users.
</p>
  
<hr />
<h1 align = "center">
    Project Structure:
  </h1>
 <ul>
  <li>
    Deviency__Score: contains support functions for the 
  </li>
  <li>
    MatLab and Computer Vision
  </li>
  <li>
    Documentation and Research
  </li>
  <li>
    Web Development
  </li>
</ul>

<!--MACHINE LEARNING AND DATA ANALYSIS TEAM --> 

<hr />
<br />
<h2 align = "center">
   Machine Learning and Data Analysis Team
</h2>
  

<h2>Responsibilities</h2>

  <!--RESPONSIBILITIES --> 
  
  <ul>
    <li>
      Filter the Mimic-iii database for patient data that can retroactively be used in data analysis
    </li>
    <li>
      Using a covariance matrix and other statistical analysis methods, uncover any factors that are major predictors of cardiovascular complications
    </li>
    <li>
      Apply machine learning algorithms to test how predictive they are compared to our statistical models
    </li>
    <li>
      Analyze our results and dataset to see if they can be better refined and support our claim that hemodynamics can be confidently used to predict patient outcome
    </li>
    <li>
      Repeat the process using the insight we acquired through our previous executions
    </li>
  </ul>
  
<h2>Technologies Used</h2>
  <!--RESPONSIBILITIES --> 
  
  <ul>
      <li>
        SQL:
        <ul>
          <li>Used to sort and structure data from our database</li>
        </ul>
      </li>
      <li>
        PostgreSQL:
        <ul>
          <li>Initially used to host our database. We have sinced found that Google's BigQuery is a better alternative
        </ul>
      </li>
      <li>
        BigQuery:
        <ul>
          <li>Used to host and filter data from the Mimic-iii Database</li>
        </ul>
      </li>
      <li>
        Google Colabs:
        <ul>
          <li>To perform machine learning and data analysis</li>
        </ul>
      </li>
      <li>
        Python:
        <ul>
          <li>Used as our primary language for data analysis. The following <strong>libraries</strong> were used for our research:</li>
            <ul>
              <strong><li>pandas</li>
                      <li>numpy</li>
                      <li>matplotlib</li>
                      <li>sklearn</li>
              </strong>
            </ul>
        </ul>
      </li>
      <li>
        Google Drive:
        <ul>
          <li>We heavily utilized Google Docs and Google Sheets to helpt store important information and share our research results</li>
        </ul>
      </li>
      <li>
        JavaScript:
        <ul>
          <li>Used to help format data and write RegEX modifiers for BigQuery</li>
        </ul>
      </li>
</ul>
  
<h3>Procedure</h3>
  <!-- PROCEDURES --> 
    <ol>
      <li>
        Acquire access to the Mimic-iii patient dataset by completing the <a href = 'https://physionet.org/about/citi-course/'>following certificate courses</a>:
          <ul>
            <li>Biomedical Responsible Conduct of Research</li>
            <li>Data or Specimens Only Research</li>
        </ul>
      </li>
      <li>
        Create a www.physionet.org account and request access to the <a href = 'https://physionet.org/content/mimiciii/1.4/'>BigQuery dataset</a>
      </li>
      <li>
        <h4>Review the database model and try to get a sufficient understanding of the data you're working with. Use the following resources to help </h4>
        <ul>
          <li>
            <a href = 'https://cloud.githubusercontent.com/assets/26095093/23737659/454872b0-0449-11e7-987d-639b0415dca4.png'>Visual database model for Mimic-iii</a>
          </li>
          <li>
            <a href = 'https://mimic.mit.edu/docs/iii/tables/'>Mimic-iii data overview</a>
          </li>
          <li>
           <a href = 'https://docs.google.com/document/d/1XnAVE6ZXsflZ1EFHavjIf97n4u9s5m-veTv88jRoR9A/edit?usp=sharing'>Condensed data overview</a>
          </li>
        </ul>
      </li>
      <li>
        Review SQL, so you can explore and modify our data. The following are recommended tutorials and resources
        <ul>
          <li><a href = "https://www.codecademy.com/learn/learn-sql">Codecademy SQL course</a></li>
          <li><a href = "https://www.youtube.com/watch?v=p3qvj9hO_Bo">Web Dev Simplified SQL video tutorial</a></li>
          <li><a href= "https://www.w3schools.com/sql/default.asp">W3schools SQL cheatsheets and references </a></li>
        </ul>
      </li>
      <li>
        Choose a database to manage your data. Unless you have a particularly powerful computer, you should not host your own database. The Mimic-iii database has over 40GB worth of data points. <strong><a href = "https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-dr-skws-all-solutions-trial-e-gcp-1010042&utm_content=text-ad-none-any-DEV_c-CRE_335630919804-ADGP_Hybrid%20%7C%20SKWS%20-%20EXA%20%7C%20Txt%20~%20Data%20Analytics%20~%20BigQuery%23v4-KWID_43700053283638057-kwd-47616965283-userloc_1007978&utm_term=KW_bigquery-NET_g-PLAC_&ds_rl=1242850&ds_rl=1245734&ds_rl=1242850&ds_rl=1245734&gclid=EAIaIQobChMI7ruNvrfx8QIVafx3Ch10NAgCEAAYASAAEgKph_D_BwE&gclsrc=aw.ds">BigQuery has been used for the project so far and has an intuitive to use UI. To use BigQuery, it'd be helpful to have access to the company's GCP account.</a></strong>
      </li>
      <li>
        Filter patients for those with evident cardiovascular problems for future analysis. Allowing patients with irrelevant health complications into the analysis will create noise. Picking only patients that have too many health complications would also result in skewed data that would make our model less predictive. To rule out bias, it's important to filter with multiple parameters.
      </li>
      <li>
        Once a sufficient population has been selected, collect chart data, as well as demographic data, such as gender, age, and ethnicity
      </li>
      <li>
        Create a covariance matrix to test for any correlations between patient data and imminient cardiovascular complications. 
      </li>
      <li>
        Test for any meaningful predictors using other statistical analysis methods and machine learning methods. Most of this has been executed on <a href = "https://colab.research.google.com/?utm_source=scs-index">Google Colabs in Python</a>; however, <a href = "https://azure.microsoft.com/en-us/services/machine-learning/">Azure Machine Learning Studio</a> (you may want to try the Classic version) and <a href = "https://www.google.com/search?q=gcp+machine+learnign&oq=gcp+machine+learnign&aqs=edge..69i57j0i22i30l2.13419j0j4&sourceid=chrome&ie=UTF-8">GCP's machine learning products may also be of interest</a>
      </li>
      <li>
        Review our results, gather insight, and refine our approach and dataset appropriately
      </li>
    </ol>
  
  
<h3>Progress</h3>
  <!--PROGRESS --> 
  
  <p>
    From a database of ~46,000 patients, we were able to find 552 patients that showed significant signs of cardiovascular complications. We used the following signifiers to isolate relevant patients: DRG codes, diagnosis-related groups; CPT events, current procedural terminology; and the perscription of pharmacueticals associated with circulitory problems. An attempt was made to use ICD9 codes, international classification of disease codes, to isolate relevant patients, but because of Mimic-iii's ICD9 formatting and the overwhelming variety of codes to look through, this approach became unfeasible for our time frame. In future iterations of our analysis, we are likely to focus more on patients with targeted chart data, but for an initial analysis, a broad approach was necessary.
  </p>
  <p>
    We created a series of tables containing all demographic variables, and averaged, quantifiable chart data. Using the [insert relevant libraries here], we created a few covariant matrixes, and are working to isolate the most relevant variables for our machine learning model. Because of the vast quanity of data we are using, it is necessary that we limit them in someway, without compromising its integrity. Current attempts involved restricting chart data to only the last 24 recorded hours, averaging data by the hour, and restricting variables only to those most universal amongst patiefnts. This procedure is standard and requires the expertise in multiple fields: database management, general programming, statistical analysis, and biology. Our results so far are promising.
  </p>
<h3>Next Major Step</h3></li>
Continue refining data, and adjusting our model to improve our results

