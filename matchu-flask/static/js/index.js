 
      //Hard-coded data which will be populated with a database
      $('#cboProjects').change(function() {
        opt = $(this).val();
        console.log(opt);
        if (opt=="1"){
          $('#msgbox').html('<p>You chose: Student Matching System</p><p>Every semester, students in CIS4935 are confronted with the task of finding other students with whom they can work. This is a multifactor matching problem.  Your job will be to create a system whereby students can all enter their preferences and it will produce the "best matches" for the course given certain constraints.  You will need to consider the following preferences:  project preferences, time-of-day availability, preference for synchronous versus asynchronous collaboration, and other things that I probably havent thought of. I could envision students being required to enter their data on the first few days of courses and the system then autoproducing a list of maximally compatible teams.  Whatever is developed should be designed so that it could live on USFs systems.  Not all matching means that the students should have the same skills (e.g. you wouldnt want a team composed of only database experts; some skills are complementary). </p><p><i>Pillars: Programming, Human-Computer Interfaces</i></p>');      
        }
        else if (opt=="2"){
          $('#msgbox').html('<p>You chose: Mesh network sensor array</p><p>Visualize an empty field.  Throughout that field, you have low-cost sensors that are connected to low-cost processes (e.g. arduinos or Raspberry Pis). They are configured in a mesh network. The sensors measure and can reproduce the movements of animals and people who enter and exit the field. The output is to a website that graphically displays recorded "events" where events are entries and exits of animals or people. </p><p><i>Pillars: Network, Programming, Human-Computer Interfaces</i></p>');
        }
        else if (opt=="3"){
          $('#msgbox').html('<p>You chose: Build a thoroughly redundant network</p><p>Using equipment that you will need to purchase, build a network that is redundant at layer 2 (Ethernet), layer 3 (TCP/IP), network services (e.g. DNS, DHCP) and at the application level.  To successfully complete this project you must demonstrate how your network can withstand multiple simultaneous failures while keeping the application functional.  You must also demonstrate redundancy at every layer of the network stack (physical, LAN, network (IP), and server/application). </p><p><i>Pillars: Networking</i></p>');     
        }
        else if (opt=="4"){
          $('#msgbox').html('<p>You chose: Status reporting system for CIS4935</p><p>Ive contemplated having students complete status reports every week for CIS4935; Canvas would not be a good tool for this.  Therefore, Im putting this out there as a potential project.  Create a system that will remind each student to complete a status report weekly of their contributions to their teams projects.  The system should email them and remind them to enter their status report if they fail do to so by a specified time.  The system should allow other members of their team, the professor and the TA to see their status reports (but not other teams). Whatever is developed should be designed so that it could live on USFs systems.</p><p><i>Pillars: Programming, Database, Cybersecurity, Human-Computer Interfaces</i></p>');
          
          //This is a card which might be used to hold groups and their information on the teacher/admin panel - probably wont be on this page
          $('#msgbox').append('<div class="row"><div class="col-sm-3 m-auto"><div class="card" style="width: 18rem;"><div class="card-body"><h5 class="card-title">Status reporting system for CIS4935 <small>Group 1</small</h5><p class="card-text mt-2"><i class="fa fa-plus"></i> Front-End - 0/1</p><p class="card-text"><i class="fa fa-plus"></i> Back-End - 0/1</p><p class="card-text"><i class="fa fa-plus"></i> Project Manager - 0/1</p><p class="card-text"><i class="fa fa-plus"></i> Other - 0/1</p></div></div><a href="#" class="btn btn-primary mt-2">Start new group</a></div></div>');
        }
      })
      
      
      $('#cboRoles').change(function() {
        //Hard-coded - These value's will also be populated from a database depending on Project selected above
        opt = $(this).val();
        console.log(opt);
        if (opt=="Front End"){
          $('#msgboxRoles').html('<p>Front End Developers are computer programmers who specialize in website design. Front End Developer duties include determining the structure and design of web pages, striking a balance between functional and aesthetic design and ensuring web design is optimized for smartphones.</p>');
        }  
        if (opt=="Back End"){
          $('#msgboxRoles').html('<p>A back-end web developer is responsible for server-side web application logic and integration of the work front-end developers do. Back-end developers usually write the web services and APIs used by front-end developers and mobile application developers.</p>');
        }  
        if (opt=="Project Manager"){
          $('#msgboxRoles').html('<p>A project manager oversees the process of planning and executing and delegating responsibilities around the organizations IT pursuits and goals. So some of the job skills they look for is someone with technical management and a technical understanding.</p>');
        }  
      })
      
      //This adds the 'selected' class to whichever day the user clicks and then shows the corresponding hour selection div
      $('.workingDayBG').click(function() {
        $(this).toggleClass('selected');
        day = $(this).attr("id");
        $('#'+day+'Hours').collapse('toggle');
        $
      })

      // API Documentation on timepicker - http://www.jonthornton.com/jquery-timepicker/
      $('.txtTime').timepicker();
      
      //Bootstrap tooltip enabler
      $(function () {
        $('[data-toggle="tooltip"]').tooltip()
      })
    