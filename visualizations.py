import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime

global_data = {'NewConfirmed': 198996, 'TotalConfirmed': 131539636, 'NewDeaths': 3923, 'TotalDeaths': 2857906, 'NewRecovered': 119884, 'TotalRecovered': 74751948, 'Date': datetime.datetime(2021, 4, 6, 7, 3, 37, 654000)}
df = pd.DataFrame.from_dict(list(global_data.items()))
df.columns = ['Concept', 'Value']

global_data_2= {"ID":"0120a464-3d82-496c-9997-6305c08d686d","Message":"","Global":{"NewConfirmed":295493,"TotalConfirmed":131637603,"NewDeaths":4288,"TotalDeaths":2858368,"NewRecovered":170027,"TotalRecovered":74802091,"Date":"2021-04-06T21:27:45.857Z"},"Countries":[{"ID":"4fe2a547-cb84-4564-85cc-2b6681306c41","Country":"Afghanistan","CountryCode":"AF","Slug":"afghanistan","NewConfirmed":0,"TotalConfirmed":56717,"NewDeaths":0,"TotalDeaths":2508,"NewRecovered":0,"TotalRecovered":51902,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"8d769540-184f-445c-9d2f-9556655b1034","Country":"Albania","CountryCode":"AL","Slug":"albania","NewConfirmed":0,"TotalConfirmed":126795,"NewDeaths":0,"TotalDeaths":2274,"NewRecovered":0,"TotalRecovered":94431,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"585e59ff-aba8-40e5-8330-55ce480f425a","Country":"Algeria","CountryCode":"DZ","Slug":"algeria","NewConfirmed":0,"TotalConfirmed":117739,"NewDeaths":0,"TotalDeaths":3108,"NewRecovered":0,"TotalRecovered":81994,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e0c59214-d928-49f9-8607-c2c1dde8f39d","Country":"Andorra","CountryCode":"AD","Slug":"andorra","NewConfirmed":0,"TotalConfirmed":12286,"NewDeaths":0,"TotalDeaths":117,"NewRecovered":0,"TotalRecovered":11523,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c7389ec4-3743-4c77-8b06-a59eb39ede29","Country":"Angola","CountryCode":"AO","Slug":"angola","NewConfirmed":0,"TotalConfirmed":22717,"NewDeaths":0,"TotalDeaths":543,"NewRecovered":0,"TotalRecovered":21452,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"a37702d7-4ca3-4f07-ba00-403e7db2a356","Country":"Antigua and Barbuda","CountryCode":"AG","Slug":"antigua-and-barbuda","NewConfirmed":0,"TotalConfirmed":1173,"NewDeaths":0,"TotalDeaths":29,"NewRecovered":0,"TotalRecovered":885,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"7798bef8-78a3-4678-9cb7-82d64292cfcc","Country":"Argentina","CountryCode":"AR","Slug":"argentina","NewConfirmed":0,"TotalConfirmed":2407159,"NewDeaths":0,"TotalDeaths":56471,"NewRecovered":0,"TotalRecovered":2153509,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"195928b5-f992-48f6-a9bc-96ca2fce67d7","Country":"Armenia","CountryCode":"AM","Slug":"armenia","NewConfirmed":0,"TotalConfirmed":197113,"NewDeaths":0,"TotalDeaths":3614,"NewRecovered":0,"TotalRecovered":176889,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"daea129d-71f4-4932-bec1-955dcf8fca2a","Country":"Australia","CountryCode":"AU","Slug":"australia","NewConfirmed":8,"TotalConfirmed":29365,"NewDeaths":0,"TotalDeaths":909,"NewRecovered":16,"TotalRecovered":23048,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"d7b2cec1-ec8c-40f3-b1bd-4604b59a3fdf","Country":"Austria","CountryCode":"AT","Slug":"austria","NewConfirmed":0,"TotalConfirmed":560972,"NewDeaths":0,"TotalDeaths":9482,"NewRecovered":0,"TotalRecovered":516084,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"8eb7a284-5fb8-47e7-9ceb-baf533363283","Country":"Azerbaijan","CountryCode":"AZ","Slug":"azerbaijan","NewConfirmed":0,"TotalConfirmed":271834,"NewDeaths":0,"TotalDeaths":3711,"NewRecovered":0,"TotalRecovered":242293,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c6235769-5bcf-4f3e-a745-93f37ef90299","Country":"Bahamas","CountryCode":"BS","Slug":"bahamas","NewConfirmed":0,"TotalConfirmed":9171,"NewDeaths":0,"TotalDeaths":188,"NewRecovered":0,"TotalRecovered":8676,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3640b3e7-5fc9-4f10-91a4-e75987544212","Country":"Bahrain","CountryCode":"BH","Slug":"bahrain","NewConfirmed":0,"TotalConfirmed":149791,"NewDeaths":0,"TotalDeaths":541,"NewRecovered":0,"TotalRecovered":139205,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ed89b5f7-1b72-4646-893d-b6ff4415e835","Country":"Bangladesh","CountryCode":"BD","Slug":"bangladesh","NewConfirmed":0,"TotalConfirmed":644439,"NewDeaths":0,"TotalDeaths":9318,"NewRecovered":0,"TotalRecovered":555414,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"dd61b240-edaf-4fec-80e6-aa50c8fdb53a","Country":"Barbados","CountryCode":"BB","Slug":"barbados","NewConfirmed":0,"TotalConfirmed":3679,"NewDeaths":0,"TotalDeaths":43,"NewRecovered":0,"TotalRecovered":3534,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3a3c08b9-e8f4-4db4-a779-acf857b5c747","Country":"Belarus","CountryCode":"BY","Slug":"belarus","NewConfirmed":0,"TotalConfirmed":328290,"NewDeaths":0,"TotalDeaths":2294,"NewRecovered":0,"TotalRecovered":318756,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"449176a4-720f-4f69-8b46-93d1d405afc5","Country":"Belgium","CountryCode":"BE","Slug":"belgium","NewConfirmed":1968,"TotalConfirmed":902964,"NewDeaths":33,"TotalDeaths":23202,"NewRecovered":0,"TotalRecovered":0,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"0dd98671-1885-4632-b0b6-9b228f9c1f84","Country":"Belize","CountryCode":"BZ","Slug":"belize","NewConfirmed":0,"TotalConfirmed":12456,"NewDeaths":0,"TotalDeaths":317,"NewRecovered":0,"TotalRecovered":12090,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"558c49ab-c15a-4e12-be54-cd38601d817a","Country":"Benin","CountryCode":"BJ","Slug":"benin","NewConfirmed":0,"TotalConfirmed":7313,"NewDeaths":0,"TotalDeaths":93,"NewRecovered":0,"TotalRecovered":6452,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"59f58453-1f7b-41da-b5a8-f5241f1c1e81","Country":"Bhutan","CountryCode":"BT","Slug":"bhutan","NewConfirmed":0,"TotalConfirmed":891,"NewDeaths":0,"TotalDeaths":1,"NewRecovered":0,"TotalRecovered":870,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5d02fbf8-43b8-440a-bfd1-706fbc4464ad","Country":"Bolivia","CountryCode":"BO","Slug":"bolivia","NewConfirmed":0,"TotalConfirmed":275392,"NewDeaths":0,"TotalDeaths":12344,"NewRecovered":0,"TotalRecovered":225483,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"af12de35-8b88-485c-8141-1e9dbbcfd51b","Country":"Bosnia and Herzegovina","CountryCode":"BA","Slug":"bosnia-and-herzegovina","NewConfirmed":0,"TotalConfirmed":176413,"NewDeaths":0,"TotalDeaths":6953,"NewRecovered":0,"TotalRecovered":133262,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"f7c7fbd9-4703-4076-b59c-ca351050ac63","Country":"Botswana","CountryCode":"BW","Slug":"botswana","NewConfirmed":0,"TotalConfirmed":41710,"NewDeaths":0,"TotalDeaths":616,"NewRecovered":0,"TotalRecovered":36958,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"66aa78f9-848d-4114-866c-f98f0299607e","Country":"Brazil","CountryCode":"BR","Slug":"brazil","NewConfirmed":28645,"TotalConfirmed":13013601,"NewDeaths":1319,"TotalDeaths":332752,"NewRecovered":61951,"TotalRecovered":11405558,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e8ba62f4-ac3c-4457-a361-263096accb2b","Country":"Brunei Darussalam","CountryCode":"BN","Slug":"brunei","NewConfirmed":0,"TotalConfirmed":214,"NewDeaths":0,"TotalDeaths":3,"NewRecovered":0,"TotalRecovered":197,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"91973940-08cb-4452-9c9a-b3e612b9c29f","Country":"Bulgaria","CountryCode":"BG","Slug":"bulgaria","NewConfirmed":0,"TotalConfirmed":356859,"NewDeaths":0,"TotalDeaths":13786,"NewRecovered":0,"TotalRecovered":273429,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"126516d7-1106-4174-b222-b66439f50de4","Country":"Burkina Faso","CountryCode":"BF","Slug":"burkina-faso","NewConfirmed":0,"TotalConfirmed":12825,"NewDeaths":0,"TotalDeaths":150,"NewRecovered":0,"TotalRecovered":12477,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"791b6c14-0b5c-48a3-968f-ef2157568efe","Country":"Burundi","CountryCode":"BI","Slug":"burundi","NewConfirmed":0,"TotalConfirmed":2964,"NewDeaths":0,"TotalDeaths":6,"NewRecovered":0,"TotalRecovered":773,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e6e5adee-9e11-4dcc-967b-11c3ece5631c","Country":"Cambodia","CountryCode":"KH","Slug":"cambodia","NewConfirmed":0,"TotalConfirmed":2752,"NewDeaths":0,"TotalDeaths":21,"NewRecovered":0,"TotalRecovered":1747,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"62accf22-5b99-4e76-a843-bb9ca2530177","Country":"Cameroon","CountryCode":"CM","Slug":"cameroon","NewConfirmed":0,"TotalConfirmed":57337,"NewDeaths":0,"TotalDeaths":851,"NewRecovered":0,"TotalRecovered":35261,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"36539234-69c2-425f-bbe3-b33a6bc41b7f","Country":"Canada","CountryCode":"CA","Slug":"canada","NewConfirmed":5435,"TotalConfirmed":863910,"NewDeaths":19,"TotalDeaths":21084,"NewRecovered":6653,"TotalRecovered":937403,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c29ef4ce-d462-4558-8342-ccc295fce5ee","Country":"Cape Verde","CountryCode":"CV","Slug":"cape-verde","NewConfirmed":0,"TotalConfirmed":17939,"NewDeaths":0,"TotalDeaths":173,"NewRecovered":0,"TotalRecovered":16587,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"80d640dc-ab3e-4aaa-93cb-2b253b02ad2f","Country":"Central African Republic","CountryCode":"CF","Slug":"central-african-republic","NewConfirmed":0,"TotalConfirmed":5313,"NewDeaths":0,"TotalDeaths":73,"NewRecovered":0,"TotalRecovered":5024,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"a6ab07bd-ec85-4000-a977-c94d11349790","Country":"Chad","CountryCode":"TD","Slug":"chad","NewConfirmed":0,"TotalConfirmed":4595,"NewDeaths":0,"TotalDeaths":166,"NewRecovered":0,"TotalRecovered":4215,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9c10320c-c0e3-4af6-a0b1-8030d589eff4","Country":"Chile","CountryCode":"CL","Slug":"chile","NewConfirmed":5827,"TotalConfirmed":1032612,"NewDeaths":33,"TotalDeaths":23677,"NewRecovered":7241,"TotalRecovered":965641,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3ac4e8db-60de-4a96-b097-5cc98caf6596","Country":"China","CountryCode":"CN","Slug":"china","NewConfirmed":40,"TotalConfirmed":101901,"NewDeaths":0,"TotalDeaths":4841,"NewRecovered":21,"TotalRecovered":96640,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"399696fd-329c-41c4-84aa-b0ffe9483481","Country":"Colombia","CountryCode":"CO","Slug":"colombia","NewConfirmed":10190,"TotalConfirmed":2456409,"NewDeaths":199,"TotalDeaths":64293,"NewRecovered":8269,"TotalRecovered":2325833,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ef4e8a7b-210f-480d-aa05-4c5bd75908a4","Country":"Comoros","CountryCode":"KM","Slug":"comoros","NewConfirmed":0,"TotalConfirmed":3725,"NewDeaths":0,"TotalDeaths":146,"NewRecovered":0,"TotalRecovered":3539,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"83d591dc-6866-42c2-9785-e136833d2eb0","Country":"Congo (Brazzaville)","CountryCode":"CG","Slug":"congo-brazzaville","NewConfirmed":0,"TotalConfirmed":9681,"NewDeaths":0,"TotalDeaths":135,"NewRecovered":0,"TotalRecovered":8208,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"349af74b-5419-42bf-b9fc-f61f6e353bb1","Country":"Congo (Kinshasa)","CountryCode":"CD","Slug":"congo-kinshasa","NewConfirmed":0,"TotalConfirmed":28354,"NewDeaths":0,"TotalDeaths":745,"NewRecovered":0,"TotalRecovered":25587,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fdddb536-0d26-4691-bb65-ce1b1c35b9c2","Country":"Costa Rica","CountryCode":"CR","Slug":"costa-rica","NewConfirmed":0,"TotalConfirmed":216764,"NewDeaths":0,"TotalDeaths":2957,"NewRecovered":0,"TotalRecovered":192699,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ce0a2617-06e9-4088-9f4f-51ad31a91563","Country":"Croatia","CountryCode":"HR","Slug":"croatia","NewConfirmed":0,"TotalConfirmed":280164,"NewDeaths":0,"TotalDeaths":6083,"NewRecovered":0,"TotalRecovered":262227,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3133ddef-6e08-418c-a0f1-d9ca95d35b3c","Country":"Cuba","CountryCode":"CU","Slug":"cuba","NewConfirmed":0,"TotalConfirmed":80610,"NewDeaths":0,"TotalDeaths":436,"NewRecovered":0,"TotalRecovered":75127,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"817f81e1-a185-46a7-9d40-61e274d10478","Country":"Cyprus","CountryCode":"CY","Slug":"cyprus","NewConfirmed":0,"TotalConfirmed":48278,"NewDeaths":0,"TotalDeaths":262,"NewRecovered":0,"TotalRecovered":2057,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"1def420c-97e5-4eb8-b7fb-ba3240a3fbc3","Country":"Czech Republic","CountryCode":"CZ","Slug":"czech-republic","NewConfirmed":0,"TotalConfirmed":1553820,"NewDeaths":0,"TotalDeaths":27057,"NewRecovered":0,"TotalRecovered":1411748,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5c7c2673-b1e0-4fcc-bdd9-53f245a3dbaa","Country":"Côte d'Ivoire","CountryCode":"CI","Slug":"cote-divoire","NewConfirmed":0,"TotalConfirmed":44841,"NewDeaths":0,"TotalDeaths":256,"NewRecovered":0,"TotalRecovered":42438,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"b2e85803-bfe7-4472-b7ed-b812733d1cb3","Country":"Denmark","CountryCode":"DK","Slug":"denmark","NewConfirmed":0,"TotalConfirmed":234489,"NewDeaths":0,"TotalDeaths":2431,"NewRecovered":0,"TotalRecovered":222843,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6235ba68-0979-4c8b-9858-986e69cbc162","Country":"Djibouti","CountryCode":"DJ","Slug":"djibouti","NewConfirmed":0,"TotalConfirmed":8696,"NewDeaths":0,"TotalDeaths":76,"NewRecovered":0,"TotalRecovered":6791,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5413678a-dfa3-45f5-b320-98b97a95bcc2","Country":"Dominica","CountryCode":"DM","Slug":"dominica","NewConfirmed":0,"TotalConfirmed":165,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":159,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"15424731-ac01-4764-b482-9a5ce328ff03","Country":"Dominican Republic","CountryCode":"DO","Slug":"dominican-republic","NewConfirmed":0,"TotalConfirmed":254435,"NewDeaths":0,"TotalDeaths":3351,"NewRecovered":0,"TotalRecovered":214512,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"acefcff7-9c88-44d0-a958-401df0a22a10","Country":"Ecuador","CountryCode":"EC","Slug":"ecuador","NewConfirmed":0,"TotalConfirmed":336777,"NewDeaths":0,"TotalDeaths":16987,"NewRecovered":0,"TotalRecovered":290314,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"473cef60-709c-451b-86e0-8ec543c8401e","Country":"Egypt","CountryCode":"EG","Slug":"egypt","NewConfirmed":0,"TotalConfirmed":205732,"NewDeaths":0,"TotalDeaths":12210,"NewRecovered":0,"TotalRecovered":156574,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"f0006e49-245f-464d-aabc-f2d57d208573","Country":"El Salvador","CountryCode":"SV","Slug":"el-salvador","NewConfirmed":0,"TotalConfirmed":65491,"NewDeaths":0,"TotalDeaths":2030,"NewRecovered":0,"TotalRecovered":62340,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"b6db123f-1544-4901-b267-da947bbc906a","Country":"Equatorial Guinea","CountryCode":"GQ","Slug":"equatorial-guinea","NewConfirmed":0,"TotalConfirmed":7059,"NewDeaths":0,"TotalDeaths":104,"NewRecovered":0,"TotalRecovered":6683,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ef4de82b-b8ed-4b3d-bacc-0af9d35f8bd4","Country":"Eritrea","CountryCode":"ER","Slug":"eritrea","NewConfirmed":0,"TotalConfirmed":3340,"NewDeaths":0,"TotalDeaths":10,"NewRecovered":0,"TotalRecovered":3064,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9d01f2e4-9638-4fca-bf23-09c19830f592","Country":"Estonia","CountryCode":"EE","Slug":"estonia","NewConfirmed":0,"TotalConfirmed":109781,"NewDeaths":0,"TotalDeaths":950,"NewRecovered":0,"TotalRecovered":87092,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"1015dbba-0bf0-48aa-9512-c646c426f5cf","Country":"Ethiopia","CountryCode":"ET","Slug":"ethiopia","NewConfirmed":0,"TotalConfirmed":217327,"NewDeaths":0,"TotalDeaths":3000,"NewRecovered":0,"TotalRecovered":163022,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"1a2d1022-35c6-4e1c-93ed-afac51d4d146","Country":"Fiji","CountryCode":"FJ","Slug":"fiji","NewConfirmed":0,"TotalConfirmed":67,"NewDeaths":0,"TotalDeaths":2,"NewRecovered":0,"TotalRecovered":64,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"4ff2cf31-fea8-42e7-a3da-8bd4a20a9f75","Country":"Finland","CountryCode":"FI","Slug":"finland","NewConfirmed":0,"TotalConfirmed":79737,"NewDeaths":0,"TotalDeaths":846,"NewRecovered":0,"TotalRecovered":46000,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"cac3883d-79de-4ed3-9e27-8043a5c63728","Country":"France","CountryCode":"FR","Slug":"france","NewConfirmed":0,"TotalConfirmed":4893971,"NewDeaths":0,"TotalDeaths":97005,"NewRecovered":0,"TotalRecovered":306893,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"8a9d79f7-2cf0-43fe-a95b-4db06173a521","Country":"Gabon","CountryCode":"GA","Slug":"gabon","NewConfirmed":0,"TotalConfirmed":19863,"NewDeaths":0,"TotalDeaths":119,"NewRecovered":0,"TotalRecovered":16910,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"0a496634-7b4c-4eb9-8143-cf776b11574d","Country":"Gambia","CountryCode":"GM","Slug":"gambia","NewConfirmed":0,"TotalConfirmed":5505,"NewDeaths":0,"TotalDeaths":166,"NewRecovered":0,"TotalRecovered":5086,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"110fce79-7f8d-4c75-9162-ece65a0cc2d1","Country":"Georgia","CountryCode":"GE","Slug":"georgia","NewConfirmed":0,"TotalConfirmed":284061,"NewDeaths":0,"TotalDeaths":3822,"NewRecovered":0,"TotalRecovered":275024,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"f4403ecd-3e25-44f6-8a20-6272d67297a0","Country":"Germany","CountryCode":"DE","Slug":"germany","NewConfirmed":5980,"TotalConfirmed":2902309,"NewDeaths":76,"TotalDeaths":77136,"NewRecovered":1730,"TotalRecovered":2587580,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6ca95073-5c19-4bf6-9819-f50d27ac4697","Country":"Ghana","CountryCode":"GH","Slug":"ghana","NewConfirmed":0,"TotalConfirmed":90900,"NewDeaths":0,"TotalDeaths":752,"NewRecovered":0,"TotalRecovered":88674,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fb8e04be-af39-44bf-be80-ebc884f758c7","Country":"Greece","CountryCode":"GR","Slug":"greece","NewConfirmed":0,"TotalConfirmed":277277,"NewDeaths":0,"TotalDeaths":8453,"NewRecovered":0,"TotalRecovered":93764,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"dbbfbbc7-3bd6-428c-942b-2438f1d8eba3","Country":"Grenada","CountryCode":"GD","Slug":"grenada","NewConfirmed":0,"TotalConfirmed":155,"NewDeaths":0,"TotalDeaths":1,"NewRecovered":0,"TotalRecovered":152,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"feb3cfbb-dbc4-4741-888a-6438d2ab5be9","Country":"Guatemala","CountryCode":"GT","Slug":"guatemala","NewConfirmed":0,"TotalConfirmed":195680,"NewDeaths":0,"TotalDeaths":6894,"NewRecovered":0,"TotalRecovered":180527,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"cd2b88f3-9bd7-44a2-9e05-64729a41711f","Country":"Guinea","CountryCode":"GN","Slug":"guinea","NewConfirmed":0,"TotalConfirmed":20506,"NewDeaths":0,"TotalDeaths":130,"NewRecovered":0,"TotalRecovered":17995,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5c9b58bd-8657-4bd6-b4bd-4cea9829558e","Country":"Guinea-Bissau","CountryCode":"GW","Slug":"guinea-bissau","NewConfirmed":0,"TotalConfirmed":3662,"NewDeaths":0,"TotalDeaths":66,"NewRecovered":0,"TotalRecovered":3012,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fb539cac-a6bb-4f60-91aa-43662c09a1e2","Country":"Guyana","CountryCode":"GY","Slug":"guyana","NewConfirmed":0,"TotalConfirmed":10606,"NewDeaths":0,"TotalDeaths":246,"NewRecovered":0,"TotalRecovered":9289,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"be1df226-4f92-4cfc-9cc1-3d71415a9b89","Country":"Haiti","CountryCode":"HT","Slug":"haiti","NewConfirmed":0,"TotalConfirmed":12788,"NewDeaths":0,"TotalDeaths":252,"NewRecovered":0,"TotalRecovered":11317,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"cc6b4833-bc7e-4eae-b905-4cb66a499763","Country":"Holy See (Vatican City State)","CountryCode":"VA","Slug":"holy-see-vatican-city-state","NewConfirmed":0,"TotalConfirmed":27,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":15,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e26f638b-6b15-4581-b2b3-575ffddc9062","Country":"Honduras","CountryCode":"HN","Slug":"honduras","NewConfirmed":0,"TotalConfirmed":191136,"NewDeaths":0,"TotalDeaths":4681,"NewRecovered":0,"TotalRecovered":73463,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"27a4b550-71c9-4a5a-9ba8-e1af8b292092","Country":"Hungary","CountryCode":"HU","Slug":"hungary","NewConfirmed":0,"TotalConfirmed":689853,"NewDeaths":0,"TotalDeaths":21928,"NewRecovered":0,"TotalRecovered":418084,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"53d8c5be-0f47-41c0-9b71-4923eb7eefae","Country":"Iceland","CountryCode":"IS","Slug":"iceland","NewConfirmed":0,"TotalConfirmed":6225,"NewDeaths":0,"TotalDeaths":29,"NewRecovered":0,"TotalRecovered":6072,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"72cf12f3-4cb6-4ec1-850d-11e5390d222f","Country":"India","CountryCode":"IN","Slug":"india","NewConfirmed":96982,"TotalConfirmed":12686049,"NewDeaths":446,"TotalDeaths":165547,"NewRecovered":50143,"TotalRecovered":11732279,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9f390b91-2539-4908-9ade-14f038c2653b","Country":"Indonesia","CountryCode":"ID","Slug":"indonesia","NewConfirmed":0,"TotalConfirmed":1537967,"NewDeaths":0,"TotalDeaths":41815,"NewRecovered":0,"TotalRecovered":1381677,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"a7509890-cd95-4b48-8b34-4c45b46adcf6","Country":"Iran, Islamic Republic of","CountryCode":"IR","Slug":"iran","NewConfirmed":0,"TotalConfirmed":1945964,"NewDeaths":0,"TotalDeaths":63332,"NewRecovered":0,"TotalRecovered":1658978,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"532f49bf-97bb-4f4d-95e6-c7e8b93395a4","Country":"Iraq","CountryCode":"IQ","Slug":"iraq","NewConfirmed":0,"TotalConfirmed":879991,"NewDeaths":0,"TotalDeaths":14502,"NewRecovered":0,"TotalRecovered":784199,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"332365cf-6535-4fc7-bacd-e438286507e3","Country":"Ireland","CountryCode":"IE","Slug":"ireland","NewConfirmed":0,"TotalConfirmed":238466,"NewDeaths":0,"TotalDeaths":4718,"NewRecovered":0,"TotalRecovered":23364,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"35908234-acf2-4a91-988d-01993fd55293","Country":"Israel","CountryCode":"IL","Slug":"israel","NewConfirmed":0,"TotalConfirmed":834603,"NewDeaths":0,"TotalDeaths":6248,"NewRecovered":0,"TotalRecovered":823330,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6528d228-f8b2-422f-9970-f76bf0d23f32","Country":"Italy","CountryCode":"IT","Slug":"italy","NewConfirmed":10680,"TotalConfirmed":3678944,"NewDeaths":296,"TotalDeaths":111326,"NewRecovered":9323,"TotalRecovered":2997522,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"a5d6b565-7cc3-4abf-a48b-cdd821d32abb","Country":"Jamaica","CountryCode":"JM","Slug":"jamaica","NewConfirmed":0,"TotalConfirmed":41013,"NewDeaths":0,"TotalDeaths":618,"NewRecovered":0,"TotalRecovered":18297,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"627681a6-87a3-40cc-baaf-c9c1f5fc67c9","Country":"Japan","CountryCode":"JP","Slug":"japan","NewConfirmed":1566,"TotalConfirmed":486792,"NewDeaths":19,"TotalDeaths":9229,"NewRecovered":1531,"TotalRecovered":451999,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"2efc3627-02df-4277-b116-f06da8499482","Country":"Jordan","CountryCode":"JO","Slug":"jordan","NewConfirmed":0,"TotalConfirmed":639444,"NewDeaths":0,"TotalDeaths":7283,"NewRecovered":0,"TotalRecovered":552764,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"256cfed7-97d6-4175-abbe-50210c33d647","Country":"Kazakhstan","CountryCode":"KZ","Slug":"kazakhstan","NewConfirmed":0,"TotalConfirmed":307676,"NewDeaths":0,"TotalDeaths":3249,"NewRecovered":0,"TotalRecovered":275505,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"80cbe6d0-2aa4-4068-8a71-aa7109256de2","Country":"Kenya","CountryCode":"KE","Slug":"kenya","NewConfirmed":0,"TotalConfirmed":139448,"NewDeaths":0,"TotalDeaths":2244,"NewRecovered":0,"TotalRecovered":94361,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fc013cf8-2249-4a9e-98a4-5391a2114e55","Country":"Korea (South)","CountryCode":"KR","Slug":"korea-south","NewConfirmed":0,"TotalConfirmed":106230,"NewDeaths":0,"TotalDeaths":1752,"NewRecovered":0,"TotalRecovered":97363,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ec0ba316-1892-43f8-bef8-47bf7757ce35","Country":"Kuwait","CountryCode":"KW","Slug":"kuwait","NewConfirmed":0,"TotalConfirmed":238549,"NewDeaths":0,"TotalDeaths":1365,"NewRecovered":0,"TotalRecovered":223269,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"40deee93-4ef9-4b60-be7d-84e228bcd278","Country":"Kyrgyzstan","CountryCode":"KG","Slug":"kyrgyzstan","NewConfirmed":0,"TotalConfirmed":89153,"NewDeaths":0,"TotalDeaths":1507,"NewRecovered":0,"TotalRecovered":85271,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6832b965-e2f8-434d-befe-bf81ac3d2501","Country":"Lao PDR","CountryCode":"LA","Slug":"lao-pdr","NewConfirmed":0,"TotalConfirmed":49,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":46,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"b237ffe7-ab71-4354-8ffa-9d2779876bc0","Country":"Latvia","CountryCode":"LV","Slug":"latvia","NewConfirmed":0,"TotalConfirmed":104224,"NewDeaths":0,"TotalDeaths":1934,"NewRecovered":0,"TotalRecovered":95561,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"35bb73d5-35d7-4a1b-91cd-97e8b98461b3","Country":"Lebanon","CountryCode":"LB","Slug":"lebanon","NewConfirmed":0,"TotalConfirmed":480502,"NewDeaths":0,"TotalDeaths":6443,"NewRecovered":0,"TotalRecovered":386768,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ae6bc5b5-a1c6-4dc2-875b-e8b3eed9322e","Country":"Lesotho","CountryCode":"LS","Slug":"lesotho","NewConfirmed":0,"TotalConfirmed":10707,"NewDeaths":0,"TotalDeaths":315,"NewRecovered":0,"TotalRecovered":4471,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"f3ad0e57-41e4-40c1-a9b9-4ed2efc1c8f7","Country":"Liberia","CountryCode":"LR","Slug":"liberia","NewConfirmed":0,"TotalConfirmed":2042,"NewDeaths":0,"TotalDeaths":85,"NewRecovered":0,"TotalRecovered":1899,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"f75e97ed-e5fa-4e2e-8d3c-73676b867f21","Country":"Libya","CountryCode":"LY","Slug":"libya","NewConfirmed":0,"TotalConfirmed":163442,"NewDeaths":0,"TotalDeaths":2757,"NewRecovered":0,"TotalRecovered":149836,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"89861846-94b5-4692-88af-9806cdf4b34d","Country":"Liechtenstein","CountryCode":"LI","Slug":"liechtenstein","NewConfirmed":0,"TotalConfirmed":2697,"NewDeaths":0,"TotalDeaths":56,"NewRecovered":0,"TotalRecovered":2571,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"dc6f2099-7de9-4338-a078-3ff970c557a0","Country":"Lithuania","CountryCode":"LT","Slug":"lithuania","NewConfirmed":0,"TotalConfirmed":220212,"NewDeaths":0,"TotalDeaths":3615,"NewRecovered":0,"TotalRecovered":201727,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"29e4f1e9-019f-4984-854a-a7d41cd45bdb","Country":"Luxembourg","CountryCode":"LU","Slug":"luxembourg","NewConfirmed":0,"TotalConfirmed":62105,"NewDeaths":0,"TotalDeaths":750,"NewRecovered":0,"TotalRecovered":57596,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"60c663a6-a8ae-4632-b204-c454412ecf4f","Country":"Macedonia, Republic of","CountryCode":"MK","Slug":"macedonia","NewConfirmed":0,"TotalConfirmed":135167,"NewDeaths":0,"TotalDeaths":3977,"NewRecovered":0,"TotalRecovered":110388,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3ceacc11-76fd-4299-82a1-751536c0f123","Country":"Madagascar","CountryCode":"MG","Slug":"madagascar","NewConfirmed":0,"TotalConfirmed":25709,"NewDeaths":0,"TotalDeaths":459,"NewRecovered":0,"TotalRecovered":22702,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fd998465-4afa-4c20-83a1-fcd770318ffe","Country":"Malawi","CountryCode":"MW","Slug":"malawi","NewConfirmed":0,"TotalConfirmed":33673,"NewDeaths":0,"TotalDeaths":1124,"NewRecovered":0,"TotalRecovered":30757,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"0e1b0e84-f6f6-4da1-8edc-946268f7cb71","Country":"Malaysia","CountryCode":"MY","Slug":"malaysia","NewConfirmed":0,"TotalConfirmed":352029,"NewDeaths":0,"TotalDeaths":1295,"NewRecovered":0,"TotalRecovered":336456,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"f7caf252-9310-4809-a445-3219dd1686e8","Country":"Maldives","CountryCode":"MV","Slug":"maldives","NewConfirmed":0,"TotalConfirmed":24908,"NewDeaths":0,"TotalDeaths":67,"NewRecovered":0,"TotalRecovered":21773,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6d7a5775-53bc-447e-9c43-0803c2d63724","Country":"Mali","CountryCode":"ML","Slug":"mali","NewConfirmed":0,"TotalConfirmed":10620,"NewDeaths":0,"TotalDeaths":393,"NewRecovered":0,"TotalRecovered":6989,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"672b14f7-5dc2-44aa-ae8b-ca1ce76046ba","Country":"Malta","CountryCode":"MT","Slug":"malta","NewConfirmed":0,"TotalConfirmed":29279,"NewDeaths":0,"TotalDeaths":399,"NewRecovered":0,"TotalRecovered":28349,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"47da76c6-36ab-4894-8394-d48901c80e0c","Country":"Marshall Islands","CountryCode":"MH","Slug":"marshall-islands","NewConfirmed":0,"TotalConfirmed":4,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":4,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"80710d46-3628-4396-ac02-0856e63c4bbe","Country":"Mauritania","CountryCode":"MR","Slug":"mauritania","NewConfirmed":0,"TotalConfirmed":17939,"NewDeaths":0,"TotalDeaths":449,"NewRecovered":0,"TotalRecovered":17212,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"786ae245-e287-44d3-a8f4-57d591552029","Country":"Mauritius","CountryCode":"MU","Slug":"mauritius","NewConfirmed":0,"TotalConfirmed":1121,"NewDeaths":0,"TotalDeaths":12,"NewRecovered":0,"TotalRecovered":707,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9e277e53-7f68-4559-9457-492a245276ae","Country":"Mexico","CountryCode":"MX","Slug":"mexico","NewConfirmed":1247,"TotalConfirmed":2251705,"NewDeaths":252,"TotalDeaths":204399,"NewRecovered":0,"TotalRecovered":1765244,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9a47745d-238f-495e-9c73-5a1edf512b66","Country":"Micronesia, Federated States of","CountryCode":"FM","Slug":"micronesia","NewConfirmed":0,"TotalConfirmed":1,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":1,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"d932866d-3560-4503-973c-20df2cc63d81","Country":"Moldova","CountryCode":"MD","Slug":"moldova","NewConfirmed":0,"TotalConfirmed":235790,"NewDeaths":0,"TotalDeaths":5178,"NewRecovered":0,"TotalRecovered":216478,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"183a0872-e6f9-472e-9e8d-54035d7d77f7","Country":"Monaco","CountryCode":"MC","Slug":"monaco","NewConfirmed":0,"TotalConfirmed":2334,"NewDeaths":0,"TotalDeaths":30,"NewRecovered":0,"TotalRecovered":2190,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"8144aaf2-c176-4752-986d-08af049cebfd","Country":"Mongolia","CountryCode":"MN","Slug":"mongolia","NewConfirmed":0,"TotalConfirmed":11651,"NewDeaths":0,"TotalDeaths":13,"NewRecovered":0,"TotalRecovered":6010,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"004f6d1e-db41-4ea3-9d23-d50bcaa7ee91","Country":"Montenegro","CountryCode":"ME","Slug":"montenegro","NewConfirmed":0,"TotalConfirmed":92740,"NewDeaths":0,"TotalDeaths":1317,"NewRecovered":0,"TotalRecovered":86029,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"52825b5c-8e56-468e-8ce8-a68645d7e638","Country":"Morocco","CountryCode":"MA","Slug":"morocco","NewConfirmed":0,"TotalConfirmed":498329,"NewDeaths":0,"TotalDeaths":8857,"NewRecovered":0,"TotalRecovered":485162,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6dda1a02-0d1f-46d4-b089-ae2e68b7f953","Country":"Mozambique","CountryCode":"MZ","Slug":"mozambique","NewConfirmed":0,"TotalConfirmed":68227,"NewDeaths":0,"TotalDeaths":782,"NewRecovered":0,"TotalRecovered":57234,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"29f10927-3d24-4202-8806-6f50d6b52a44","Country":"Myanmar","CountryCode":"MM","Slug":"myanmar","NewConfirmed":0,"TotalConfirmed":142511,"NewDeaths":0,"TotalDeaths":3206,"NewRecovered":0,"TotalRecovered":131815,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"dd242ace-6987-4eb6-a498-beab05202589","Country":"Namibia","CountryCode":"NA","Slug":"namibia","NewConfirmed":0,"TotalConfirmed":44886,"NewDeaths":0,"TotalDeaths":538,"NewRecovered":0,"TotalRecovered":42358,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5b2c7830-964e-4a73-9b98-3f545656cadb","Country":"Nepal","CountryCode":"NP","Slug":"nepal","NewConfirmed":0,"TotalConfirmed":278210,"NewDeaths":0,"TotalDeaths":3036,"NewRecovered":0,"TotalRecovered":273342,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"66072cdb-c6ae-4984-9cc3-bf37ef8585b5","Country":"Netherlands","CountryCode":"NL","Slug":"netherlands","NewConfirmed":5320,"TotalConfirmed":1307466,"NewDeaths":7,"TotalDeaths":16629,"NewRecovered":0,"TotalRecovered":0,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"32f997af-1194-435e-a883-9e5db9f70048","Country":"New Zealand","CountryCode":"NZ","Slug":"new-zealand","NewConfirmed":0,"TotalConfirmed":2524,"NewDeaths":0,"TotalDeaths":26,"NewRecovered":0,"TotalRecovered":2424,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fe6f12dd-d9b0-4edb-ac97-305983cdf14c","Country":"Nicaragua","CountryCode":"NI","Slug":"nicaragua","NewConfirmed":0,"TotalConfirmed":6677,"NewDeaths":0,"TotalDeaths":178,"NewRecovered":0,"TotalRecovered":4225,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3b387239-2971-4b3b-adb9-3fc4a08bdae7","Country":"Niger","CountryCode":"NE","Slug":"niger","NewConfirmed":0,"TotalConfirmed":5041,"NewDeaths":0,"TotalDeaths":188,"NewRecovered":0,"TotalRecovered":4698,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"58a0b011-b102-42b3-a375-16b203f4530c","Country":"Nigeria","CountryCode":"NG","Slug":"nigeria","NewConfirmed":0,"TotalConfirmed":163330,"NewDeaths":0,"TotalDeaths":2058,"NewRecovered":0,"TotalRecovered":152045,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"97ea575f-a702-47c2-a6ef-504c5da04901","Country":"Norway","CountryCode":"NO","Slug":"norway","NewConfirmed":0,"TotalConfirmed":99249,"NewDeaths":0,"TotalDeaths":676,"NewRecovered":0,"TotalRecovered":17998,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e77b6c47-fc9d-4b09-84aa-c5dc8e94d6d2","Country":"Oman","CountryCode":"OM","Slug":"oman","NewConfirmed":0,"TotalConfirmed":164274,"NewDeaths":0,"TotalDeaths":1722,"NewRecovered":0,"TotalRecovered":147539,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"56b89921-c57c-40b9-b06a-295a7d9fe1bd","Country":"Pakistan","CountryCode":"PK","Slug":"pakistan","NewConfirmed":3953,"TotalConfirmed":696184,"NewDeaths":103,"TotalDeaths":14924,"NewRecovered":2198,"TotalRecovered":618158,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e7d65045-4fcf-4a1f-8f9b-c964cee7e162","Country":"Palestinian Territory","CountryCode":"PS","Slug":"palestine","NewConfirmed":0,"TotalConfirmed":253922,"NewDeaths":0,"TotalDeaths":2716,"NewRecovered":0,"TotalRecovered":223249,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c510aa0c-4320-4068-a34e-59874bfeef95","Country":"Panama","CountryCode":"PA","Slug":"panama","NewConfirmed":0,"TotalConfirmed":356556,"NewDeaths":0,"TotalDeaths":6138,"NewRecovered":0,"TotalRecovered":345719,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"944aa699-1f2d-4c41-8c37-fb4f80e5b52c","Country":"Papua New Guinea","CountryCode":"PG","Slug":"papua-new-guinea","NewConfirmed":0,"TotalConfirmed":7406,"NewDeaths":0,"TotalDeaths":67,"NewRecovered":0,"TotalRecovered":846,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c767be6e-4859-490f-8185-f1adf8c44aa2","Country":"Paraguay","CountryCode":"PY","Slug":"paraguay","NewConfirmed":0,"TotalConfirmed":222663,"NewDeaths":0,"TotalDeaths":4463,"NewRecovered":0,"TotalRecovered":183552,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"68df66a2-ec7b-4b63-933a-9f90f6d55763","Country":"Peru","CountryCode":"PE","Slug":"peru","NewConfirmed":7842,"TotalConfirmed":1590209,"NewDeaths":261,"TotalDeaths":53138,"NewRecovered":8911,"TotalRecovered":1509493,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"af0bbcbb-eb37-46ff-9ce4-cdb4a71fceaf","Country":"Philippines","CountryCode":"PH","Slug":"philippines","NewConfirmed":0,"TotalConfirmed":803398,"NewDeaths":0,"TotalDeaths":13435,"NewRecovered":0,"TotalRecovered":646237,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ff8a8981-f4f8-401d-8b77-baafbafd7bec","Country":"Poland","CountryCode":"PL","Slug":"poland","NewConfirmed":0,"TotalConfirmed":2448463,"NewDeaths":0,"TotalDeaths":55005,"NewRecovered":0,"TotalRecovered":2009308,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c7219e8a-9a07-4dc3-bbba-468a047a59dc","Country":"Portugal","CountryCode":"PT","Slug":"portugal","NewConfirmed":0,"TotalConfirmed":823494,"NewDeaths":0,"TotalDeaths":16885,"NewRecovered":0,"TotalRecovered":780643,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9e6dbb44-a4d2-4830-815a-ee39ba572ded","Country":"Qatar","CountryCode":"QA","Slug":"qatar","NewConfirmed":0,"TotalConfirmed":184334,"NewDeaths":0,"TotalDeaths":306,"NewRecovered":0,"TotalRecovered":166441,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6d6c2874-af46-412c-b823-a0ee4d41420a","Country":"Republic of Kosovo","CountryCode":"XK","Slug":"kosovo","NewConfirmed":0,"TotalConfirmed":91079,"NewDeaths":0,"TotalDeaths":1892,"NewRecovered":0,"TotalRecovered":75850,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5b53d851-23c1-43db-97b6-596bef96f925","Country":"Romania","CountryCode":"RO","Slug":"romania","NewConfirmed":0,"TotalConfirmed":977986,"NewDeaths":0,"TotalDeaths":24190,"NewRecovered":0,"TotalRecovered":875487,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"17df731f-6cc7-4e3e-927d-2e5e62909a03","Country":"Russian Federation","CountryCode":"RU","Slug":"russia","NewConfirmed":8525,"TotalConfirmed":4538101,"NewDeaths":336,"TotalDeaths":99049,"NewRecovered":7029,"TotalRecovered":4163170,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"60012c6f-f1d9-4909-96e5-f1a7b8f085f2","Country":"Rwanda","CountryCode":"RW","Slug":"rwanda","NewConfirmed":0,"TotalConfirmed":22684,"NewDeaths":0,"TotalDeaths":311,"NewRecovered":0,"TotalRecovered":20594,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"fc97af21-0ac8-4e1f-b248-755e18bd1614","Country":"Saint Kitts and Nevis","CountryCode":"KN","Slug":"saint-kitts-and-nevis","NewConfirmed":0,"TotalConfirmed":44,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":44,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"3f1c4229-1e4e-41f8-818c-d3e783563678","Country":"Saint Lucia","CountryCode":"LC","Slug":"saint-lucia","NewConfirmed":0,"TotalConfirmed":4273,"NewDeaths":0,"TotalDeaths":61,"NewRecovered":0,"TotalRecovered":4142,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9f6983b2-9fef-44d3-89a8-75de6f738550","Country":"Saint Vincent and Grenadines","CountryCode":"VC","Slug":"saint-vincent-and-the-grenadines","NewConfirmed":0,"TotalConfirmed":1764,"NewDeaths":0,"TotalDeaths":10,"NewRecovered":0,"TotalRecovered":1625,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"358d7cd9-92aa-4eed-ab64-e29f353e1c52","Country":"Samoa","CountryCode":"WS","Slug":"samoa","NewConfirmed":0,"TotalConfirmed":3,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":2,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"d2abf0b7-9559-4a09-bb50-af453f9bc81a","Country":"San Marino","CountryCode":"SM","Slug":"san-marino","NewConfirmed":0,"TotalConfirmed":4775,"NewDeaths":0,"TotalDeaths":84,"NewRecovered":0,"TotalRecovered":4170,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"47dde129-1cd3-41ce-ab1b-642f3a8760c2","Country":"Sao Tome and Principe","CountryCode":"ST","Slug":"sao-tome-and-principe","NewConfirmed":0,"TotalConfirmed":2244,"NewDeaths":0,"TotalDeaths":35,"NewRecovered":0,"TotalRecovered":2140,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"7a3bbc4e-5e49-4792-ad4c-bfba4d4b8e07","Country":"Saudi Arabia","CountryCode":"SA","Slug":"saudi-arabia","NewConfirmed":0,"TotalConfirmed":393377,"NewDeaths":0,"TotalDeaths":6704,"NewRecovered":0,"TotalRecovered":380305,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"cb7e0806-eec2-48b5-babc-ccba92eee051","Country":"Senegal","CountryCode":"SN","Slug":"senegal","NewConfirmed":0,"TotalConfirmed":39093,"NewDeaths":0,"TotalDeaths":1063,"NewRecovered":0,"TotalRecovered":37767,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ea9d0fd1-8d52-41c1-affa-c73d4f9704d2","Country":"Serbia","CountryCode":"RS","Slug":"serbia","NewConfirmed":0,"TotalConfirmed":621375,"NewDeaths":0,"TotalDeaths":5497,"NewRecovered":0,"TotalRecovered":0,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"d6447749-e0f3-491d-ad57-e409a7f7126c","Country":"Seychelles","CountryCode":"SC","Slug":"seychelles","NewConfirmed":0,"TotalConfirmed":4320,"NewDeaths":0,"TotalDeaths":24,"NewRecovered":0,"TotalRecovered":3869,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ab133432-7a9f-4152-af80-2b803ec6925e","Country":"Sierra Leone","CountryCode":"SL","Slug":"sierra-leone","NewConfirmed":0,"TotalConfirmed":3989,"NewDeaths":0,"TotalDeaths":79,"NewRecovered":0,"TotalRecovered":2825,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"d8e34ac3-df4a-40ab-9d48-faa8385dfa96","Country":"Singapore","CountryCode":"SG","Slug":"singapore","NewConfirmed":0,"TotalConfirmed":60495,"NewDeaths":0,"TotalDeaths":30,"NewRecovered":0,"TotalRecovered":60214,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"32aea2ca-007b-4ea5-ba35-bb23fd82efbb","Country":"Slovakia","CountryCode":"SK","Slug":"slovakia","NewConfirmed":0,"TotalConfirmed":365400,"NewDeaths":0,"TotalDeaths":10094,"NewRecovered":0,"TotalRecovered":255300,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"5d3938bc-d6a0-4106-b65d-d4d98f01f60e","Country":"Slovenia","CountryCode":"SI","Slug":"slovenia","NewConfirmed":0,"TotalConfirmed":220425,"NewDeaths":0,"TotalDeaths":4082,"NewRecovered":0,"TotalRecovered":202239,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ea7571a5-b918-4aa4-b1c1-c99968b4b9d3","Country":"Solomon Islands","CountryCode":"SB","Slug":"solomon-islands","NewConfirmed":0,"TotalConfirmed":19,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":18,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"96b2aa91-147b-4592-9847-6748dafca493","Country":"Somalia","CountryCode":"SO","Slug":"somalia","NewConfirmed":0,"TotalConfirmed":11908,"NewDeaths":0,"TotalDeaths":568,"NewRecovered":0,"TotalRecovered":5017,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"cc09c508-0b23-49a7-abdd-93b2dd76588f","Country":"South Africa","CountryCode":"ZA","Slug":"south-africa","NewConfirmed":0,"TotalConfirmed":1552416,"NewDeaths":0,"TotalDeaths":52995,"NewRecovered":0,"TotalRecovered":1478088,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"24ab3359-2a64-4c63-88b3-98362b716d68","Country":"South Sudan","CountryCode":"SS","Slug":"south-sudan","NewConfirmed":0,"TotalConfirmed":10281,"NewDeaths":0,"TotalDeaths":113,"NewRecovered":0,"TotalRecovered":9835,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"395a520c-05eb-4c76-92e7-693289129a34","Country":"Spain","CountryCode":"ES","Slug":"spain","NewConfirmed":10360,"TotalConfirmed":3311325,"NewDeaths":85,"TotalDeaths":75783,"NewRecovered":0,"TotalRecovered":150376,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"aa128dda-ad43-48e6-afcd-e1c1e6198bee","Country":"Sri Lanka","CountryCode":"LK","Slug":"sri-lanka","NewConfirmed":0,"TotalConfirmed":93595,"NewDeaths":0,"TotalDeaths":581,"NewRecovered":0,"TotalRecovered":90563,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"312da8d1-dafa-4c4e-ac85-2b63317c6e07","Country":"Sudan","CountryCode":"SD","Slug":"sudan","NewConfirmed":0,"TotalConfirmed":31833,"NewDeaths":0,"TotalDeaths":2063,"NewRecovered":0,"TotalRecovered":24214,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"7179c488-3aaf-4d12-908c-70d2f20cd1a8","Country":"Suriname","CountryCode":"SR","Slug":"suriname","NewConfirmed":0,"TotalConfirmed":9174,"NewDeaths":0,"TotalDeaths":177,"NewRecovered":0,"TotalRecovered":8633,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"8a7544b7-6f33-4322-a286-03247d1888cc","Country":"Swaziland","CountryCode":"SZ","Slug":"swaziland","NewConfirmed":0,"TotalConfirmed":17354,"NewDeaths":0,"TotalDeaths":669,"NewRecovered":0,"TotalRecovered":16618,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"c409ec4a-9433-43d7-b073-2f3d03f6faf1","Country":"Sweden","CountryCode":"SE","Slug":"sweden","NewConfirmed":0,"TotalConfirmed":813191,"NewDeaths":0,"TotalDeaths":13498,"NewRecovered":0,"TotalRecovered":0,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e6d1ac7a-ead5-4f13-8da1-298e46048797","Country":"Switzerland","CountryCode":"CH","Slug":"switzerland","NewConfirmed":0,"TotalConfirmed":605342,"NewDeaths":0,"TotalDeaths":10377,"NewRecovered":0,"TotalRecovered":317600,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"339b91ae-4e50-44ab-b4f6-ea3158031f52","Country":"Syrian Arab Republic (Syria)","CountryCode":"SY","Slug":"syria","NewConfirmed":0,"TotalConfirmed":19526,"NewDeaths":0,"TotalDeaths":1323,"NewRecovered":0,"TotalRecovered":13316,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e53194d5-c98d-46a2-838a-1058c27f103c","Country":"Taiwan, Republic of China","CountryCode":"TW","Slug":"taiwan","NewConfirmed":0,"TotalConfirmed":1048,"NewDeaths":0,"TotalDeaths":10,"NewRecovered":0,"TotalRecovered":1004,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e551a898-6f2f-4d41-9e23-de63c21fe267","Country":"Tajikistan","CountryCode":"TJ","Slug":"tajikistan","NewConfirmed":0,"TotalConfirmed":13308,"NewDeaths":0,"TotalDeaths":90,"NewRecovered":0,"TotalRecovered":13218,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"50bc96b4-9045-42c2-8816-c041d07ecaa3","Country":"Tanzania, United Republic of","CountryCode":"TZ","Slug":"tanzania","NewConfirmed":0,"TotalConfirmed":509,"NewDeaths":0,"TotalDeaths":21,"NewRecovered":0,"TotalRecovered":183,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"1e5bfef2-9995-493f-a2bb-59cb155ca007","Country":"Thailand","CountryCode":"TH","Slug":"thailand","NewConfirmed":0,"TotalConfirmed":29321,"NewDeaths":0,"TotalDeaths":95,"NewRecovered":0,"TotalRecovered":26873,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"0a697ccc-5246-4649-b1a0-dd18f052912c","Country":"Timor-Leste","CountryCode":"TL","Slug":"timor-leste","NewConfirmed":0,"TotalConfirmed":766,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":294,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"1d8bcc4c-ccdb-45d0-aeb4-566193901922","Country":"Togo","CountryCode":"TG","Slug":"togo","NewConfirmed":0,"TotalConfirmed":11249,"NewDeaths":0,"TotalDeaths":112,"NewRecovered":0,"TotalRecovered":8348,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"1729771c-1507-43a9-a065-bdde929cc10c","Country":"Trinidad and Tobago","CountryCode":"TT","Slug":"trinidad-and-tobago","NewConfirmed":0,"TotalConfirmed":8192,"NewDeaths":0,"TotalDeaths":145,"NewRecovered":0,"TotalRecovered":7665,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"d9c6c03b-759f-4747-ac98-a01b7c516f00","Country":"Tunisia","CountryCode":"TN","Slug":"tunisia","NewConfirmed":0,"TotalConfirmed":261177,"NewDeaths":0,"TotalDeaths":8993,"NewRecovered":0,"TotalRecovered":219912,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"7efe4bb9-d222-42e1-a2f4-31713ac3501f","Country":"Turkey","CountryCode":"TR","Slug":"turkey","NewConfirmed":0,"TotalConfirmed":3529601,"NewDeaths":0,"TotalDeaths":32456,"NewRecovered":0,"TotalRecovered":3130977,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"91b0a1b5-c781-498c-9856-42eb2331f19e","Country":"Uganda","CountryCode":"UG","Slug":"uganda","NewConfirmed":0,"TotalConfirmed":41016,"NewDeaths":0,"TotalDeaths":335,"NewRecovered":0,"TotalRecovered":40452,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ba66b02c-987e-4f62-ac11-0873396c5ca7","Country":"Ukraine","CountryCode":"UA","Slug":"ukraine","NewConfirmed":10300,"TotalConfirmed":1807327,"NewDeaths":261,"TotalDeaths":36255,"NewRecovered":4969,"TotalRecovered":1400102,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"008bdea1-d313-43ac-8a2f-ab93011d7010","Country":"United Arab Emirates","CountryCode":"AE","Slug":"united-arab-emirates","NewConfirmed":0,"TotalConfirmed":472148,"NewDeaths":0,"TotalDeaths":1512,"NewRecovered":0,"TotalRecovered":456747,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"e22702cc-c342-4a5a-bce9-6b82eb1670f3","Country":"United Kingdom","CountryCode":"GB","Slug":"united-kingdom","NewConfirmed":2831,"TotalConfirmed":4376629,"NewDeaths":28,"TotalDeaths":127106,"NewRecovered":42,"TotalRecovered":13296,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"8324b34c-3e62-4423-854e-8038a4018ef9","Country":"United States of America","CountryCode":"US","Slug":"united-states","NewConfirmed":77794,"TotalConfirmed":30785390,"NewDeaths":515,"TotalDeaths":555613,"NewRecovered":0,"TotalRecovered":0,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"bac15689-8d43-49a4-937e-ce32c5d3c7ea","Country":"Uruguay","CountryCode":"UY","Slug":"uruguay","NewConfirmed":0,"TotalConfirmed":119958,"NewDeaths":0,"TotalDeaths":1146,"NewRecovered":0,"TotalRecovered":94042,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"b1a718ff-edc9-4637-9d53-56c1f85b530d","Country":"Uzbekistan","CountryCode":"UZ","Slug":"uzbekistan","NewConfirmed":0,"TotalConfirmed":83802,"NewDeaths":0,"TotalDeaths":631,"NewRecovered":0,"TotalRecovered":81763,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"ad909f8c-b9ca-4eb1-a8bf-a01a2841b0b4","Country":"Vanuatu","CountryCode":"VU","Slug":"vanuatu","NewConfirmed":0,"TotalConfirmed":3,"NewDeaths":0,"TotalDeaths":0,"NewRecovered":0,"TotalRecovered":1,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9f7c61e6-1869-4115-a1cc-597dc14742e2","Country":"Venezuela (Bolivarian Republic)","CountryCode":"VE","Slug":"venezuela","NewConfirmed":0,"TotalConfirmed":167548,"NewDeaths":0,"TotalDeaths":1678,"NewRecovered":0,"TotalRecovered":152201,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"6454d1d2-7d63-4a3a-8948-ac8892113a9d","Country":"Viet Nam","CountryCode":"VN","Slug":"vietnam","NewConfirmed":0,"TotalConfirmed":2637,"NewDeaths":0,"TotalDeaths":35,"NewRecovered":0,"TotalRecovered":2416,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"32e504c4-e735-4e24-b826-85eb7681f541","Country":"Yemen","CountryCode":"YE","Slug":"yemen","NewConfirmed":0,"TotalConfirmed":4881,"NewDeaths":0,"TotalDeaths":955,"NewRecovered":0,"TotalRecovered":1772,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"cb1316b5-f4a7-44d0-857b-c9daac104b01","Country":"Zambia","CountryCode":"ZM","Slug":"zambia","NewConfirmed":0,"TotalConfirmed":89009,"NewDeaths":0,"TotalDeaths":1222,"NewRecovered":0,"TotalRecovered":85178,"Date":"2021-04-06T21:27:45.857Z","Premium":{}},{"ID":"9d5a1b74-3871-4395-a60c-4dbdd8fb7771","Country":"Zimbabwe","CountryCode":"ZW","Slug":"zimbabwe","NewConfirmed":0,"TotalConfirmed":36934,"NewDeaths":0,"TotalDeaths":1525,"NewRecovered":0,"TotalRecovered":34758,"Date":"2021-04-06T21:27:45.857Z","Premium":{}}],"Date":"2021-04-06T21:27:45.857Z"}
df2 = pd.DataFrame(global_data_2['Countries'])


def create_card(value, text):
    fig = go.Figure(go.Indicator(
        value = value,
        title = {"text": str(text)}
    ))

    fig.update_layout(paper_bgcolor = "lightgray", height= 200)

    return fig


def create_map(df, target):

    fig  = go.Figure(
                    data=go.Choropleth(
                    locations=df['Country'],
                    z = df[str(target)],
                    locationmode = 'country names',
                    colorscale = 'Burg',
                    colorbar_title = str(target),
                ),
                layout = go.Layout(
                    geo=dict(bgcolor= 'rgba(0,0,0,0)'),
                    font = {"size": 14, "color":"White"},
                    margin={"r":0,"t":40,"l":0,"b":0},
                    paper_bgcolor='#4E5D6C',
                    plot_bgcolor='#4E5D6C',
                )
            )
    return fig


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'Coronavirus Tracker' # what appears on tab and google search

# app.layout = html.Div(
#     children=[
#         html.Div(
#             children=[
#                 html.P(children='🦠', className='header-emoji'),
#                 html.H1(children='Coronavirus Tracker', className='header-title'),
#                 html.P(children='In this section you will find a series of visualizations describing the evolution of the coronavirus.', className='header-description')
#             ],
#             className='header',
#         ),
#         html.Div(
#             children=[
#                 html.H1(children='Global Cases', className='header-global-title'),
#                 html.Div(
#                     children=[
#                         html.Div(
#                             children=[
#                             html.H6(
#                                 children=('Total Confirmed'),
#                                 style={
#                                     'textAlign': 'center',
#                                     'color': 'white',
#                                     'fontSize': 15,
#                                     #'backgroundColor': '34495E',
#                                 }
#                             ),
#                             html.P(
#                                 children=[
#                                     html.P(
#                                         f'{str(global_data["TotalConfirmed"])}',
#                                         style={
#                                             'textAlign': 'center',
#                                             'color': 'orange',
#                                             'fontSize': 40
#                                         }
#                                     )
#                                 ]
#                             ),
#                             html.P(
#                                 f'New Cases: {global_data["NewConfirmed"]}',
#                                 style={
#                                     'textAlign': 'center',
#                                     'color': 'orange',
#                                     'fontSize': 20
#                                 }
#                             )
#                         ],
#                             className='card'
#                         ),
#                         html.Div(
#                             children=[
#                                 html.H6(
#                                     children=('Total Confirmed'),
#                                     style={
#                                         'textAlign': 'center',
#                                         'color': 'white',
#                                         'fontSize': 15
#                                     }
#                                 ),
#                                 html.P(
#                                     children=[
#                                         html.P(
#                                             f'{str(global_data["TotalConfirmed"])}',
#                                             style={
#                                                 'textAlign': 'center',
#                                                 'color': 'orange',
#                                                 'fontSize': 40
#                                             }
#                                         )
#                                     ]
#                                 ),
#                                 html.P(
#                                     f'New Cases: {global_data["NewConfirmed"]}',
#                                     style={
#                                         'textAlign': 'center',
#                                         'color': 'orange',
#                                         'fontSize': 20
#                                     }
#                                 )
#                             ],
#                             className='card'
#                         ),
#                         html.Div(
#                             children=[
#                                 html.H6(
#                                     children=('Total Confirmed'),
#                                     style={
#                                         'textAlign': 'center',
#                                         'color': 'white',
#                                         'fontSize': 15
#                                     }
#                                 ),
#                                 html.P(
#                                     children=[
#                                         html.P(
#                                             f'{str(global_data["TotalConfirmed"])}',
#                                             style={
#                                                 'textAlign': 'center',
#                                                 'color': 'orange',
#                                                 'fontSize': 40
#                                             }
#                                         )
#                                     ]
#                                 ),
#                                 html.P(
#                                     f'New Cases: {global_data["NewConfirmed"]}',
#                                     style={
#                                         'textAlign': 'center',
#                                         'color': 'orange',
#                                         'fontSize': 20
#                                     }
#                                 )
#                             ],
#                             className='card'
#                         )
#                     ],
#                     style={
#                         'columnCount': 3,
#                         'margin-top': '32px'
#                            },
#                 )
#
#             ],
#             className='wrapper-global-cases'
#         ),
#         html.Div(
#             children=[
#                 html.H1(children='Global Map', className='header-global-title'),
#                 html.P(children='Confirmed Cases', className='header-description'),
#                 html.Div(
#                     children=[
#                         html.Div(
#                             children=(
#                                 dcc.Graph(
#                                     id= 'Map',
#                                     figure=create_map(df2, 'TotalConfirmed')
#                                 ),
#                             ),
#                             className='map',
#                         ),
#                     ],
#                     className='wrapper-map'
#                 ),
#                 html.Div(
#                     children=(
#                         html.P('Made in Colombia by Bedo', className='header-description')
#                     ),
#                     className='header-credits'
#                 )
#             ],
#             className='wrapper-map'
#         ),
#     ],
#     className='background'
# )
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.P(children='🦠', className='header-emoji'),
                        html.H1(children='Coronavirus Tracker', className='header-title'),
                        html.P(children='In this section you will find a series of visualizations describing the evolution of the coronavirus.', className='header-description')
                    ],
                    className='header-container'
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.H1(children='Global Information', className='header-title')
                                    ],
                                    className='cards-title'
                                ),
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H6(
                                                            children='Total Confirmed',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'white',
                                                                'fontSize': 15
                                                            }
                                                        ),
                                                        html.P(
                                                            children='El numero aqui',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'orange',
                                                                'fontSize': 40
                                                            }
                                                        ),
                                                        html.P(
                                                            children='Nuevos casos',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'orange',
                                                                'fontSize': 20
                                                            }
                                                        )
                                                    ],
                                                    className='four columns' # Card 1
                                                ),
                                                    html.Div(
                                                    children=[
                                                        html.H6(
                                                            children='Total Confirmed',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'white',
                                                                'fontSize': 15
                                                            }
                                                        ),
                                                        html.P(
                                                            children='El numero aqui',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'orange',
                                                                'fontSize': 40
                                                            }
                                                        ),
                                                        html.P(
                                                            children='Nuevos casos',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'orange',
                                                                'fontSize': 20
                                                            }
                                                        )
                                                    ],
                                                    className='four columns' # Card 2
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.H6(
                                                            children='Total Confirmed',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'white',
                                                                'fontSize': 15
                                                            }
                                                        ),
                                                        html.P(
                                                            children='El numero aqui',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'orange',
                                                                'fontSize': 40
                                                            }
                                                        ),
                                                        html.P(
                                                            children='Nuevos casos',
                                                            style={
                                                                'textAlign': 'center',
                                                                'color': 'orange',
                                                                'fontSize': 20
                                                            }
                                                        )
                                                    ],
                                                    className='four columns' # Card 3
                                                ),
                                            ]
                                        )
                                    ],
                                    className='row', # the three cards
                                )
                            ],
                            className='cards-container'
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.H1(children='Global Map', className='header-global-title'),
                                        html.P(children='Confirmed Cases', className='header-description'),
                                    ],
                                    className='map-title'
                                ),
                                html.Div(
                                    children=[
                                        dcc.Graph(
                                            id= 'map_figure',
                                            figure= create_map(df2, 'TotalConfirmed')
                                        )
                                    ],
                                    className='map-fig'
                                )
                            ],
                            className='map-container'
                        )
                    ],
                    className='charts-container'
                ),
                html.Div(
                    children=[
                        html.P('Made in Colombia by Bedo', className='header-description')
                    ],
                    className='credits-container'
                )
            ],
            className='block-container'
        )
    ],
    className='background'
)

if __name__ == '__main__':
    app.run_server(debug=True)