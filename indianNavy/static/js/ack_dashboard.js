 
$(window).on('load',function(){
 $.ajax({
                  url:  '/acknowledge/ack_detail/',
                  type: "GET",
                  dataType: "json",
                  //data:{"parent_id":"parent_id"},
                   success: function(response){

                   
                    var arr = [];
                    var arrCount = []
                    policy_name = []
                    policy_count = []
                    publication_name = []
                    publication_count = []
                    for(var i=0;i<response.length;i++){
                      //alert(JSON.stringify(response))
                      var public_data = i+1
                      
                      arr.push(response[i]['menu_name'])
                      

                      
                        $('#ack_bar').append(` <li class="col-sm-2" style="color:#000" ><a href="${response[i]['url_link']}" style="color:#000;">${response[i]['menu_name']}</a><br/><hr>
                        </li>` )
                        if (response[i]['menu_name'] =='Policy Letters')
                        {
                          arrCount.push(response[i]['ask_submenues'].length)

                          var obj_length = response[i]['ask_submenues'].length
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="zoom-in-right"
                           data-aos-easing="ease-out-cubic"
                           data-aos-duration="2000"><aside id="sidebar" class="left-bar">
                           <div class="feature-matchs"><h4  style="border-bottom:1px dotted grey; background-color: #f39c12; color:#fff;
                            font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><div class="col-lg-12 col-sm-12 col-xs-12"><div class="col-lg-5 col-sm-12 col-xs-12">
                           <h3>Total : ${obj_length}</h3></div><div class="col-lg-7 col-sm-12 col-xs-12">&nbsp;</div></div><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                    border: none;
                              color: white;
                              padding: 10px 20px;
                              text-align: center;
                              text-decoration: none;
                              display: inline-block;
                              font-size: 16px;
                              margin: 0px 2px;
                              cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                          if (obj_length > 0)
                        {
                          var dashboard = '#dashbdcount_'+public_data
                            //$('#myUL').empty()
                             // for (var polkk = 0; polkk<response[i]['ask_submenues'].length;polkk++)

                             // {
                               
                               
                             //   plocy_size =  response[i]['ask_submenues'][polkk]['policy_name'].length
                             //   if (plocy_size > 0)
                             //   {
                             //    policy_count.push(response[i]['ask_submenues'][polkk]['policy_name'].length)
                             //    //for (var poli_size = 0;poli_size<plocy_size;poli_size++ )
                             //    //{
                             //      policy_name.push(response[i]['ask_submenues'][polkk]['policy_name'][0]['policy_name'])
                             //    //}
                             //   }
                             // }
                        for (var kk = 0; kk<response[i]['ascsubmenu_count'].length;kk++)
                        {
                            
                             if (kk % 2 ==0)
                          {
                            $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" data-aos="flip-right"
                       data-aos-easing="ease-out-cubic"
                       data-aos-duration="2000" style="padding-top:3%; border-bottom:1px solid #8080802e"  ><div class="col-lg-2 col-sm-2 col-xs-2"><i class="fa fa-file-pdf-o grens" style="font-size:15px;color:#57cdfb; border: 1px solid #ddd;
                                                border-radius: 4px;
                                                padding: 5px;
                                                width: auto; border-color: #57cdfb; padding:10px; 10px  10px 10px"></i> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000; text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical;">${response[i]['ascsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascsubmenu_count'][kk]['added_on']}</p></div></div>`)
                                               


                                      ////////////////////////////////////////////index.page///////////


                                      $('#ack_mens').append(`<div class="col-lg-12 col-sm-12 col-xs-12" data-aos="flip-right"
                       data-aos-easing="ease-out-cubic"
                       data-aos-duration="2000" style="padding-top:3%; border-bottom:1px solid #8080802e"  ><div class="col-lg-2 col-sm-2 col-xs-2"><i class="fa fa-file-pdf-o grens" style="font-size:15px;color:#57cdfb; border: 1px solid #ddd;
                                                border-radius: 4px;
                                                padding: 5px;
                                                width: auto; border-color: #57cdfb; padding:10px; 10px  10px 10px"></i> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000; text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical;">${response[i]['ascsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascsubmenu_count'][kk]['added_on']}</p></div></div>`)
                                               




                                                                   
                                            }
                                            else
                                            {


                                              $('#ack_mens').append(`<div class="col-lg-12 col-sm-12 col-xs-12" data-aos="flip-right"
                       data-aos-easing="ease-out-cubic"
                       data-aos-duration="2000" style="padding-top:3%; border-bottom:1px solid #8080802e"  ><div class="col-lg-2 col-sm-2 col-xs-2"><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                                border-radius: 4px;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i>  </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical;">${response[i]['ascsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascsubmenu_count'][kk]['added_on']}</p></div></div>`)
                                     


                                              $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" data-aos="flip-right"
                       data-aos-easing="ease-out-cubic"
                       data-aos-duration="2000" style="padding-top:3%; border-bottom:1px solid #8080802e"  ><div class="col-lg-2 col-sm-2 col-xs-2"><i class="fa fa-file-pdf-o oranges" style="font-size:15px;color:#FF6347; border: 1px solid #ddd;
                                                border-radius: 4px;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; padding:10px; 10px  10px 10px"></i>  </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical;">${response[i]['ascsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascsubmenu_count'][kk]['added_on']}</p></div></div>`)
                                          
                                            }
                          


                        }
                        if (response[i]['ask_submenues'].length > 0)
                        {
                           for (var kk = 0; kk<response[i]['ask_submenues'].length;kk++)
                        {
                          
                            // $('#myUL').append(`<li><input type="radio" id="aa_${response[i]['ask_submenues'][kk]['id']}" value="${response[i]['ask_submenues'][0]['submenu_name']}" name="megafol" class="box" onclick="dsd(this.id,this.className)" >${response[i]['ask_submenues'][0]['submenu_name']}
                            //   <ul class="nested" id="nested_${response[i]['ask_submenues'][kk]['id']}">
                            // </ul>                     </li>`)
                        }
                        }
                      }
                        }
                        if (response[i]['menu_name'] =='Publications')
                        {
                          var obj_length = response[i]['ask_subpublicationmenues'].length
                          arrCount.push(response[i]['ask_subpublicationmenues'].length)
                          

                          // $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4"><aside id="sidebar" class="left-bar"><div class="feature-matchs"><h4 style="border-bottom:1px dotted grey; background-color: #bdc3c7; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><h3>Total : ${obj_length}</h3><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                          //     border: none;
                          //     color: white;
                          //     padding: 10px 20px;
                          //     text-align: center;
                          //     text-decoration: none;
                          //     display: inline-block;
                          //     font-size: 16px;
                          //     margin: 0px 2px;
                          //     cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="flip-left"
                     data-aos-easing="ease-out-cubic"
                      data-aos-duration="2000"><aside id="sidebar" class="left-bar">
                      <div class="feature-matchs">
                      <h4  style="border-bottom:1px dotted grey; background-color: #008dd2; color:#fff; font-weight:bold">
                       ${response[i]['menu_name']}</h4><div class="team-btw-match" ><div class="col-lg-12 col-sm-12 col-xs-12">
                       <div class="col-lg-5 col-sm-12 col-xs-12">
                       <h3>Total : ${obj_length}</h3></div><div class="col-lg-7 col-sm-12 col-xs-12">
                       </div></div><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                              border: none;
                              color: white;
                              padding: 10px 20px;
                              text-align: center;
                              text-decoration: none;
                              display: inline-block;
                              font-size: 16px;
                              margin: 0px 2px;
                              cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                           if (obj_length > 0)
                              {
                                var dashboard = '#dashbdcount_'+public_data
                                for (var kk = 0; kk<response[i]['ascpublicationsubmenu_count'].length;kk++)
                                  {
                                    if (response[i]['ascpublicationsubmenu_count'][kk]['publicationfile'] != null)
                                           {
                                            var files = response[i]['ascpublicationsubmenu_count'][kk]['publicationfile'].split(".")
                                            var image_file = files.length-1
                                            images = files[image_file]
                                            
                                           }
                                     if (kk % 2 ==0)
                                {
                                 if ((images =='png') || (images =='PNG') || (images =='JPEG') || (images =='jpg'))
                                            {

                                              var img  = `<img class="img grens" src="http://192.168.0.6:8088${response[i]['ascpublicationsubmenu_count'][kk]['publicationfile']}" width="40px"; height="40px" style="padding:15px; 15px  15px 15px; color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                              border-radius: 100%;
                              padding: 5px;
                              width: auto; border-color: #57cdfb; background-color:#8080802e"  >`

                                            }
                                            else
                                            {
                                              img = `&nbsp;`
                                            }

                                  
                                  $('#publicitiesdocument').append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%; border-bottom:1px solid #8080802e" >
                                    <div class="col-lg-2 col-sm-2 col-xs-2">  ${img}
                                     </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                             text-overflow: ellipsis;
                             display: -webkit-box;
                             -webkit-line-clamp: 1; /* number of lines to show */
                             -webkit-box-orient: vertical;">${response[i]['ascpublicationsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascpublicationsubmenu_count'][kk]['added_on']}</p></div></div>`)

////////////////////////////////////////////////////End of home page//////////////////////
                                   $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%; border-bottom:1px solid #8080802e" >
                                    <div class="col-lg-2 col-sm-2 col-xs-2">  ${img}
                                     </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                             text-overflow: ellipsis;
                             display: -webkit-box;
                             -webkit-line-clamp: 1; /* number of lines to show */
                             -webkit-box-orient: vertical;">${response[i]['ascpublicationsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascpublicationsubmenu_count'][kk]['added_on']}</p></div></div>`)
                                           
                              
                                }
                                else
                                {

                                   if ((images =='png') || (images =='PNG') || (images =='JPEG') || (images =='jpg'))
                                            {
                                              var img  = `<img class="img oranges" src="http://192.168.0.6:8088${response[i]['ascpublicationsubmenu_count'][kk]['publicationfile']}" width="40px"; height="40px" style="padding:15px; 15px  15px 15px; color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                              border-radius: 100%;
                              padding: 5px;
                              width: auto; border-color: #f7b7c2; background-color:#f7e5e58a"  >`

                                            }
                                            else
                                            {
                                              img = `&nbsp;`
                                            }

                                              $('#publicitiesdocument').append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%; border-bottom:1px solid #8080802e" >
                                    <div class="col-lg-2 col-sm-2 col-xs-2">  ${img}
                                     </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                             text-overflow: ellipsis;
                             display: -webkit-box;
                             -webkit-line-clamp: 1; /* number of lines to show */
                             -webkit-box-orient: vertical;">${response[i]['ascpublicationsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascpublicationsubmenu_count'][kk]['added_on']}</p></div></div>`)



                                            ///////////////////////end of home page
                                   $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%; border-bottom:1px solid #8080802e;" >
                                    <div class="col-lg-2 col-sm-2 col-xs-2">${img} </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                                   text-overflow: ellipsis;
                                   display: -webkit-box;
                                   -webkit-line-clamp: 1; /* number of lines to show */
                                   -webkit-box-orient: vertical;">${response[i]['ascpublicationsubmenu_count'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascpublicationsubmenu_count'][kk]['added_on']}</p></div></div>`)
                                                 
                                 

                                }
                                  }

                        }
                         
                        }
                        



// {
// }


                    ///////////////////////?Guidelines////////////////////////

                     if (response[i]['menu_name'] =='Guidelines')
                        {
                          var obj_length = response[i]['ascguideleinessubmenu_count']['menu']
                          arrCount.push(response[i]['ask_subguidelinesmenues'].length)
                          $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="zoom-out-down"
                           data-aos-easing="ease-in-cubic"
                           data-aos-duration="2000">
                           <aside id="sidebar" class="left-bar"><div class="feature-matchs">
                           <h4 style="border-bottom:1px dotted grey; background-color: #75a537; color:#fff; font-weight:bold">
                            ${response[i]['menu_name']}</h4><div class="team-btw-match" ><div class="col-lg-12 col-sm-12 col-xs-12">
                            <div class="col-lg-5 col-sm-12 col-xs-12"><h3>Total : ${obj_length}</h3></div><div class="col-lg-7 col-sm-12 col-xs-12">
                            &nbsp; </div></div><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                    border: none;
                              color: white;
                              padding: 10px 20px;
                              text-align: center;
                              text-decoration: none;
                              display: inline-block;
                              font-size: 16px;
                              margin: 0px 2px;
                              cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                           if (obj_length > 0)
                            {
                              var dashboard = '#dashbdcount_'+public_data
                              for (var kk = 0; kk<response[i]['ascguideleinessubmenu_count']['data'].length;kk++)
                              {

                                  if (response[i]['ascguideleinessubmenu_count']['data'][kk]['file'] != null)
                                           {

                                            //alert(response[i]['ascguideleinessubmenu_count']['data'][kk]['file'])  


                                            var files = response[i]['ascguideleinessubmenu_count']['data'][kk]['file'].split(".")
                                            var image_file = files.length-1
                                            images = files[image_file]
                                            
                                           }
                                           else{
                                            images = ''
                                           }
                                 // alert(JSON.stringify(response[i]['ascguideleinessubmenu_count']['data'][kk]['file']))



                                if (kk % 2 ==0)
                                {

                                  if ((images =='png') || (images =='PNG') || (images =='JPEG') || (images =='jpg'))
                                            {

                                              var img  = `<img class="img" src="http://192.168.0.6:8088${response[i]['ascguideleinessubmenu_count']['data'][kk]['file']}" width="40px"; height="40px" style="padding:15px; 15px  15px 15px; color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                              border-radius: 100%;
                              padding: 5px;
                              width: auto; border-color: #57cdfb; background-color:#f7e5e58a"  >`

                                            }
                                            else
                                            {
                                              img = `&nbsp;`
                                            }


                                  $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%; border-bottom:1px solid #8080802e" >
                                    <div class="col-lg-2 col-sm-2 col-xs-2">${img}</div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                                 text-overflow: ellipsis;
                                 display: -webkit-box;
                                 -webkit-line-clamp: 1; /* number of lines to show */
                                 -webkit-box-orient: vertical;">${response[i]['ascguideleinessubmenu_count']['data'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascguideleinessubmenu_count']['data'][kk]['added_on']}</p></div></div>`)
                                       
                       
                                    
                                }
                                else{

                                        if ((images =='png') || (images =='PNG') || (images =='JPEG') || (images =='jpg'))
                                            {
                                              var img  = `<img class="img" src="http://192.168.0.6:8088${response[i]['ascguideleinessubmenu_count']['data'][kk]['file']}" width="40px"; height="40px" style="padding:15px; 15px  15px 15px; color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                              border-radius: 100%;
                              padding: 5px;
                              width: auto; border-color: #f7b7c2; background-color:#8080802e"  >`

                                            }
                                            else
                                            {
                                              img = `&nbsp;`
                                            }



                                  $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%; border-bottom:1px solid #8080802e" >
                                    <div class="col-lg-2 col-sm-2 col-xs-2">
                                    ${img} </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" color:#000;  text-align: justify; overflow: hidden;
                               text-overflow: ellipsis;
                               display: -webkit-box;
                               -webkit-line-clamp: 1; /* number of lines to show */
                               -webkit-box-orient: vertical;">${response[i]['ascguideleinessubmenu_count']['data'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ascguideleinessubmenu_count']['data'][kk]['added_on']}</p></div></div>`)
                                       

                                }
                              }
                            

                          
                            }

                         
                         
                        }

        //////////////////////////////////////Standards///////////////////
                      if (response[i]['menu_name'] =='Standards')
                        {
                          //alert(JSON.stringify(response[i]['standards']['menu']))
                          var obj_length = response[i]['standards']['menu']
                          arrCount.push(response[i]['ask_substandardsmenues'].length)

                          // $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4"><aside id="sidebar" class="left-bar"><div class="feature-matchs"><h4 style="border-bottom:1px dotted grey; background-color: #f39c12; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><h3>Total : ${obj_length}</h3><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                          //     border: none;
                          //     color: white;
                          //     padding: 10px 20px;
                          //     text-align: center;
                          //     text-decoration: none;
                          //     display: inline-block;
                          //     font-size: 16px;
                          //     margin: 0px 2px;
                          //     cursor: pointer;" id="myBtn">Read more</button></aside></div>`)

                           $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="zoom-out-down"
                           data-aos-easing="ease-out-cubic"
                           data-aos-duration="2000"><aside id="sidebar" class="left-bar"><div class="feature-matchs"><h4 style="border-bottom:1px dotted grey; background-color: #f39c12; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><div class="col-lg-12 col-sm-12 col-xs-12"><div class="col-lg-4 col-sm-4 col-xs-4"><h3>Tot : ${obj_length}</h3></div><div class="col-lg-8 col-sm-8 col-xs-8"><img src="http://192.168.0.6:8088/static/images/standards_icon.png" width="200px" height="100px" class="rounded-circle" alt="Cinque Terre" ></div></div><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                    border: none;
                                                    color: white;
                              padding: 10px 20px;
                              text-align: center;
                              text-decoration: none;
                              display: inline-block;
                              font-size: 16px;
                              margin: 0px 2px;
                              cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                            if (obj_length > 0)
                        {
                          var dashboard = '#dashbdcount_'+public_data
                          //alert(JSON.stringify(response[i]['standards']['data']))

                        for (var kk = 0; kk<response[i]['standards']['data'].length;kk++)
                        {
                          

                           if (kk % 2 ==0)
                          {

                            $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['standards']['data'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                              border-radius: 100%;
                              padding: 5px;
                              width: auto; border-color: #f7b7c2; background-color:#4874bf"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                               text-overflow: ellipsis;
                               display: -webkit-box;
                               -webkit-line-clamp: 1; /* number of lines to show */
                               -webkit-box-orient: vertical; color:#000; "  >${response[i]['standards']['data'][kk]['folder_title']}</a><p text-align="justify">${response[i]['standards']['data'][kk]['added_on']}</p></div></div>`)

                                                      //  $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.8:8088/static/images/standardsred.png" class="rounded-circle" alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#">${response[i]['standards'][kk]['submenu_name']}</a></div></div>`)
                                                    
                                                       // $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><span style="border-bottom:1px dotted grey"><img src="http://192.168.0.8:8088/static/images/abc1.png" class="rounded-circle" alt="Cinque Terre" width="10%" height="10%"> <input type="checkbox" id="${response[i]['standards'][kk]['id']}" value="${response[i]['standards'][kk]['id']}" name="megafol" onclick="megafolder(this.id,'${response[i]['menu_name']}')"></span>${response[i]['standards'][kk]['submenu_name']}</div>`)
                                                    
                                                      }
                                                      else
                                                      {

                                                        $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['standards']['data'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                                                          border-radius: 100%;
                                                          padding: 5px;
                                                          width: auto; border-color: #f7b7c2; background-color:#bdc3c7"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                               text-overflow: ellipsis;
                               display: -webkit-box;
                               -webkit-line-clamp: 1; /* number of lines to show */
                               -webkit-box-orient: vertical; color:#000; "  >${response[i]['standards']['data'][kk]['folder_title']}</a><p text-align="justify">${response[i]['standards']['data'][kk]['added_on']}</p></div></div>`)
                                                        //$(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.8:8088/static/images/standardsblue.png" class="rounded-circle" alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#">${response[i]['standards'][kk]['submenu_name']}</a></div></div>`)
                        

                          }
                          //$(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%"><input type="checkbox" id="${response[i]['standards'][kk]['id']}" value="${response[i]['standards'][kk]['id']}" name="megafol" onclick="megafolder(this.id,'${response[i]['menu_name']}')">${response[i]['standards'][kk]['submenu_name']}</div>`)
                        }
                      }

                          

                         
                        
                        }
                        

          /////////////////////////////////////////////Navy Orders//////////////////////////
          if (response[i]['menu_name'] =='Navy Orders')
                        {
                          var obj_length = response[i]['ask_subnavy_ordersmenues'].length
                          arrCount.push(response[i]['ask_subnavy_ordersmenues'].length)

                          $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="zoom-out-left"
                           data-aos-easing="ease-in-cubic"
                           data-aos-duration="2000"><aside id="sidebar" class="left-bar">
                           <div class="feature-matchs">
                           <h4 style="border-bottom:1px dotted grey;
                            background-color: #4874bf; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4>
                            <div class="team-btw-match" ><div class="col-lg-12 col-sm-12 col-xs-12">
                            <div class="col-lg-4 col-sm-4 col-xs-4"><h3>Tot : ${obj_length}</h3></div>
                            <div class="col-lg-8 col-sm-8 col-xs-8">
                            <img src="http://192.168.0.6:8088/static/images/orders.png" width="200px" height="100px" class="rounded-circle" alt="Cinque Terre" ></div></div><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                    border: none;
                              color: white;
                              padding: 10px 20px;
                              text-align: center;
                              text-decoration: none;
                              display: inline-block;
                              font-size: 16px;
                              margin: 0px 2px;
                              cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                           if (obj_length > 0)
                        {
                          var dashboard = '#dashbdcount_'+public_data

                        for (var kk = 0; kk<response[i]['navy_ordersCount'].length;kk++)
                        {
                          
                           if (kk % 2 ==0)
                          {

                            $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" >
                              <div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['navy_ordersCount'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                              border-radius: 100%;
                              padding: 5px;
                              width: auto; border-color: #f7b7c2; background-color:#4874bf"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical; color:#000; "  >${response[i]['navy_ordersCount'][kk]['folder_title']}</a><p text-align="justify">${response[i]['navy_ordersCount'][kk]['added_on']}</p></div></div>`)
                                              
                                              
                                            }
                                            else
                                            {

                                               $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['navy_ordersCount'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                                                border-radius: 100%;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; background-color:#bdc3c7"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical; color:#000; ">${response[i]['navy_ordersCount'][kk]['folder_title']}</a><p text-align="justify">${response[i]['navy_ordersCount'][kk]['added_on']}</p></div></div>`)
                                              
                                             

                                            }
                                          }
                                        }
                                           
                                          }
                                          
                                           ///////////////////////?Navy Instructions////////////////////////

                                       if (response[i]['menu_name'] =='Navy_Instructions')
                                          {
                                           // alert(JSON.stringify(response[i]['navyInstrctionCount']))
                                            var obj_length = response[i]['navyInstrctionCount']['menu']
                                            arrCount.push(response[i]['ask_subnavy_instructionmenues'].length)

                                            $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="zoom-out-right"
                       data-aos-easing="ease-in-cubic"
                       data-aos-duration="2000"><aside id="sidebar" class="left-bar"><div class="feature-matchs"><h4 style="border-bottom:1px dotted grey; background-color: #4874bf; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><h3>Total : ${obj_length}</h3><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" ></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                border: none;
                                                color: white;
                                                padding: 10px 20px;
                                                text-align: center;
                                                text-decoration: none;
                                                display: inline-block;
                                                font-size: 16px;
                                                margin: 0px 2px;
                                                cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                                            if (obj_length > 0)
                                            {
                                              var dashboard = '#dashbdcount_'+public_data
                                              for (var kk = 0; kk<response[i]['navyInstrctionCount']['data'].length;kk++)
                                              {
                                                if (kk % 2 ==0)
                                            {

                                              $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['navyInstrctionCount']['data'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                                                border-radius: 100%;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; background-color:#4874bf"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical; color:#000; ">${response[i]['navyInstrctionCount']['data'][kk]['folder_title']}</a><p text-align="justify">${response[i]['navyInstrctionCount']['data'][kk]['added_on']}</p></div></div>`)
                                              
                                              //$(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.8:8088/static/images/instructionred.png" class="rounded-circle" alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#">${response[i]['navyInstrctionCount'][kk]['submenu_name']}</a></div></div>`)
                                          
                                              
                                            }
                                            else
                                            {
                                               $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['navyInstrctionCount']['data'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                                                border-radius: 100%;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; background-color:#bdc3c7"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical; color:#000; ">${response[i]['navyInstrctionCount']['data'][kk]['folder_title']}</a><p text-align="justify">${response[i]['navyInstrctionCount']['data'][kk]['added_on']}</p></div></div>`)
                                              
                                             // $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.8:8088/static/images/instructionred.png" class="rounded-circle" alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#">${response[i]['navyInstrctionCount'][kk]['submenu_name']}</a></div></div>`)
                                          

                                            }
                                              }
                                            }
                                           
                                          }



                                            ///////////////////////?Library////////////////////////

                                       if (response[i]['menu_name'] =='NHQ e-Library')
                                          {
                                            var obj_length = response[i]['ask_subnohqsmenues'].length
                                            arrCount.push(response[i]['ask_subnohqsmenues'].length)

                                            $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4" data-aos="zoom-out-down"
                       data-aos-easing="ease-in-cubic"
                       data-aos-duration="2000"><aside id="sidebar" class="left-bar"><div class="feature-matchs"><h4 style="border-bottom:1px dotted grey; background-color: #4874bf; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><div class="col-lg-12 col-sm-12 col-xs-12"><div class="col-lg-4 col-sm-4 col-xs-4"><h3>Tot : ${obj_length}</h3></div><div class="col-lg-8 col-sm-8 col-xs-8"><img src="http://192.168.0.6:8088/static/images/elibrary.jpg" width="200px" height="100px" class="rounded-circle" alt="Cinque Terre" ></div></div><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}"></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                border: none;
                                                color: white;
                                                padding: 10px 20px;
                                                text-align: center;
                                                text-decoration: none;
                                                display: inline-block;
                                                font-size: 16px;
                                                margin: 0px 2px;
                                                cursor: pointer;" id="myBtn">Read more</button></aside></div>`)
                                            if (obj_length > 0)
                                          {
                                            var dashboard = '#dashbdcount_'+public_data

                                          for (var kk = 0; kk<response[i]['ask_libCount'].length;kk++)
                                          {
                                            if (kk % 2 ==0)
                                            {
                                              //alert(JSON.stringify(response[i]['ask_libCount']))
                                              $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                    border-radius: 4px;
                    padding: 5px;
                    width: auto; border-color: #f7b7c2;"></i> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical; color:#000; ">${response[i]['ask_libCount'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ask_libCount'][kk]['added_on']}</p></div></div>`)
                                              

                                            }
                                            else
                                            {
                                               $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><i class="fa fa-file-pdf-o" style="font-size:36px;color:#FF6347; border: 1px solid #ddd;
                    border-radius: 4px;
                    padding: 5px;
                    width: auto; border-color: #f7b7c2;"></i> </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                     text-overflow: ellipsis;
                     display: -webkit-box;
                     -webkit-line-clamp: 1; /* number of lines to show */
                     -webkit-box-orient: vertical; color:#000; ">${response[i]['ask_libCount'][kk]['folder_title']}</a><p text-align="justify">${response[i]['ask_libCount'][kk]['added_on']}</p></div></div>`)
                                              
                                            }
                                           
                                          }
                                        }
                                          }


                                  /////////////////////////////////////////////////////////////////Brs///////////////////////////////////////

                                  if (response[i]['menu_name'] =='BRs')
                                          {
                                            var obj_length = response[i]['brsmenues'].length
                                            var lenth = 0
                                            
                                            //arrCount.push(response[i]['brsmenues'].length)
                                            arrCount.push(lenth)

                                            $('#ack_men').append(`<div class="col-lg-4 col-sm-4 col-xs-4"><aside id="sidebar" class="left-bar"><div class="feature-matchs"><h4 style="border-bottom:1px dotted grey; background-color: #4874bf; color:#fff; font-weight:bold"> ${response[i]['menu_name']}</h4><div class="team-btw-match" ><h3>Total : 0</h3><div class="col-lg-12 col-sm-12 col-xs-12" id="dashbdcount_${public_data}" ></div></div><button onclick="megamyFunction('${response[i]['menu_name']}')" class="thbg-color" style="background: #800000; background-color: #800000;
                                                border: none;
                                                color: white;
                                                padding: 10px 20px;
                                                text-align: center;
                                                text-decoration: none;
                                                display: inline-block;
                                                font-size: 16px;
                                                margin: 0px 2px;
                                                cursor: pointer;" id="myBtn">Read more</button></aside></div>`)


                                            if (obj_length > 0)
                                              {
                                                var dashboard = '#dashbdcount_'+public_data
                                                for (var kk = 0; kk<response[i]['brsCount'].length;kk++)
                                                  {
                                                   if (kk % 2 ==0)
                                            {
                                              //alert(JSON.stringify(response[i]['ask_libCount']))
                                             $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['brsCount'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                                                border-radius: 100%;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; background-color:#4874bf"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                                                 text-overflow: ellipsis;
                                                 display: -webkit-box;
                                                 -webkit-line-clamp: 1; /* number of lines to show */
                                                 -webkit-box-orient: vertical;color:#000; ">${response[i]['brsCount'][kk]['folder_title']}</a><p text-align="justify">${response[i]['brsCount'][kk]['added_on']}</p></div></div>`)
                                                                          
                                              

                                            }
                                            else
                                            {
                                               $(dashboard).append(`<div class="col-lg-12 col-sm-12 col-xs-12" style="padding-top:3%;" ><div class="col-lg-2 col-sm-2 col-xs-2"><img src="http://192.168.0.6:8088${response[i]['navyInstrctionCount']['data'][kk]['file']}" width="40px"; height="40px" style="color:#FF6347;border-radius: 100%; border: 1px solid #ddd;
                                                border-radius: 100%;
                                                padding: 5px;
                                                width: auto; border-color: #f7b7c2; background-color:#4874bf"  alt="Cinque Terre" > </div><div class="col-lg-10 col-sm-10 col-xs-10" style="align:justify"><a href="#" style=" text-align: justify; overflow: hidden;
                                                 text-overflow: ellipsis;
                                                 display: -webkit-box;
                                                 -webkit-line-clamp: 1; /* number of lines to show */
                                                 -webkit-box-orient: vertical; color:#000; ">${response[i]['brsCount'][kk]['folder_title']}</a><p text-align="justify">${response[i]['brsCount'][kk]['added_on']}</p></div></div>`)
                                                                          
                                                 
                                            }
                                }

                            }




                       
                        }

//alert(JSON.stringify(response[i]['ask_submenues']))

                      
          //             $('#myUL').append(`<li><span class="box">Green Tea</span>
          //   <ul class="nested">
          //     <li>Sencha</li>
          //     <li>Gyokuro</li>
          //     <li>Matcha</li>
          //     <li>Pi Lo Chun</li>
          //   </ul>
          // </li>`)
    //                   if (response[i]['ask_submenues'].length > 0)
    //                   {
    //                     //alert(response[i]['ask_submenues'].length)
    //                    for (var j=0; j<response[i]['ask_submenues'].length;j++)
    //                    {
    //                     $('#policy_name').append(`<tr><td><i class="fa fa-file-pdf-o" style="font-size:18px;color:red"></i>${response[i]['ask_submenues'][j]['submenu_name']}</td><td></td><td>${response[i]['ask_submenues'][j]['added_on']}</td></tr>`)
                        
    //                     $('#myULl').append(`<li><input type="checkbox" id="aa_${j}" class="box" onclick="dsd(this.id,this.className)" >${response[i]['ask_submenues'][j]['submenu_name']}
    // <ul class="nested" id="nested_${j}"></li>`)
    //                     //alert(JSON.stringify(response[i]['ask_submenues'][j]['policy_name']))
    //                     if (response[i]['ask_submenues'][j]['policy_name'].length> 0)
    //                     {
    //                        var nestedid = "#nested_"+j
    //                       for (var k=0; k<response[i]['ask_submenues'][j]['policy_name'].length;k++)
    //                       {
                           
    //                       $(nestedid).append(`<li><input type="checkbox" id="bb_${k}" class="box" onclick="dsd(this.id,this.className)" >${response[i]['ask_submenues'][j]['policy_name'][k]['policy_name']}
    // <ul class="nested" id="nested_${k}"></li>`)
    //                     } 
    //                       }
                          
    
  
    //                   // var aaaa = "aa_"+j


    //                    }
    //                   }

                    }
                   // alert(policy_name)
                   // alert(policy_count)
                    // var arr = [];
                    //var arrCount = []

                    var policydataa  = policy_name
                   var policylabels  = policy_count 

                   var dataa  = arr
                   var labels  = arrCount

                    Highcharts.chart('ccontainer', {
                       chart: {
                          type: 'column'
                        },
                        title: {
                          text: 'Km'
                      },
                       xAxis: {
                        categories:arr
                        },
                        series: [{
          name: 'KM',
          data: arrCount,
          color: 'green'
          }]

                    })
                   Highcharts.chart('policycontainer', {
      chart: {
          type: 'pie'
      },
      title: {
          text: 'Policy Graph'
      },
      xAxis: {
          categories:policydataa
        },
        series: [{
          name: 'Policy Graph',
          data: policylabels,
          color: 'green'
          }]
    })
                     
                   }
 })

})