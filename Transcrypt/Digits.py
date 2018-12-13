from JMSSGraphics import *
from JMSSNeural import *

jmss = Graphics(width = 350, height = 350, title = "Xs or Os", fps = 60)

n = 8
side_length = 32
margin = 8
border = 16

pixels = [0] * n * n

network = [[[0.9317184609443889, 0.36304956854020215, 0.49125598270681425, 0.1523725399089818, 0.9165691120899706, 0.5758601667556568, 0.5607748029978926, 0.8071055405089024, 0.4018614487707472, 0.15785966591011513, 0.2662256539196055, 0.912022685696843, 0.7108954927260814, 0.03717406558658755, 0.5291315334011221, 0.5978101127807443, 0.28352720204889786, 0.9493638096249348, 0.4648976785565582, 0.30934707579490867, 0.5845048585105804, 0.6093714061307832, 0.9700361968280317, 0.9437130747488077, 0.9884137017334353, 0.6331349046077779, 0.47840887038664714, 0.9364369707692534, 0.9683470593781333, 0.3232260979887201, 0.7355715397267717, 0.5153008968502628, 0.931124702699673, 0.6194183557455031, 0.5953210948282739, 0.5941176659756652, 0.16776107913532987, 0.779618433685449, 0.4130756534461939, 0.4380483020783756, 0.2227262232627922, 0.5595719025287292, 0.10471942382916224, 0.6012315915646683, 0.9903947348265862, 0.7359172786640708, 0.030130899834097384, 0.209418741625199, 0.7073868137992116, 0.36641723938823445, 0.4023113139908273, 0.08777777534701071, 0.3910624711379025, 0.21438733004795574, 0.07286168829687457, 0.2971251067321126, 0.39095461331278614, 0.10982785516897496, 0.8729806690442101, 0.5360930697869121, 0.7942834468357894, 0.9685461492416051, 0.26460027377486744, 0.6339460865908169, 0.8419944182578609], [0.31049020103354336, 0.34596341327816604, 0.3041904056522244, 0.35887556520602765, 0.33513054697000694, 0.30090829693341553, 0.26831616012549125, 0.2992797241557243, 0.9006821856751293, 0.0965464209962465, 0.12585991237144775, 0.21089951851495897, 0.8058932142965418, 0.059174697291536654, 0.696311522880861, 0.10912727718698238, 0.07432809511695493, 0.20269753189603396, 0.3536410563932638, 0.7359149666559068, 0.7414979401894405, 0.9489620135353845, 0.3349334596563426, 0.36203610269434044, 0.47474073316331805, 0.13594853324596923, 0.5700324392990479, 0.9441656522195193, 0.5645726280289015, 0.649626923209279, 0.3923266322538512, 0.9831354242462417, 0.19446315093641392, 0.7548165478204163, 0.967394415468054, 0.5726264370724132, 0.5453165547632923, 0.7610912362304183, 0.28778154125081445, 0.6845269332571471, 0.8358774898528123, 0.48822489690606746, 0.07166899574831906, 0.7383399244172452, 0.18434691520188895, 0.012638668590085009, 0.7113704321211213, 0.1352054499383063, 0.26346431719467184, 0.9445244385873142, 0.21534170896178473, 0.734523553703767, 0.06180767934060727, 0.23843943698254438, 0.8040890702971959, 0.420197921202605, 0.6101715885193592, 0.15597027318601525, 0.3579621264177466, 0.009328892990344515, 0.8931756689206289, 0.39014323071107243, 0.31601800329497876, 0.9700384658291046, 0.07349010248347587], [0.18715899715178774, 0.16344008832908313, 0.2871420871929444, 0.2772828970397406, 0.6534175418143573, 0.4948633896011681, 0.723657390085404, 0.9165356161286513, 0.5567474708615401, 0.17977242474458235, 0.03191054405068392, 0.5681679666325617, 0.55863457481027, 0.3340482050347647, 0.22066919418640785, 0.5523222560197364, 0.5600414308437359, 0.31622105267677864, 0.2535991625824539, 0.23080546067987023, 0.6100809722913408, 0.3321117189590422, 0.012186695703538138, 0.6519312147484219, 0.3721004890775948, 0.9780822739687461, 0.9103396959745597, 0.7698152262904985, 0.5368310686213105, 0.18286713829558107, 0.37001764694182193, 0.6445806604318852, 0.0783821458820457, 0.2455744998276441, 0.26350338568417986, 0.2013235510063968, 0.33161915701431005, 0.1696746461886424, 0.3352896299467737, 0.6002052006199066, 0.5645636607547464, 0.5754358857763372, 0.08331846029849725, 0.4537132008073513, 0.20928275015980505, 0.24161288246802806, 0.8257722507971281, 0.13755820777488548, 0.0968748451274924, 0.7202969995127503, 0.7408296633232386, 0.09459629342109016, 0.48994479627822385, 0.10670470084522793, 0.7651359697991612, 0.572614282925457, 0.16616485285307192, 0.9451033358976115, 0.023118718738526292, 0.408728163256863, 0.24548831285628123, 0.8046915836942277, 0.5689111578470889, 0.7589544226986782, 0.7255534545857757], [0.06607663749475312, 0.9370741029551323, 0.27616097413031965, 0.8011163124625824, 0.7252575864493703, 0.3854110340371066, 0.0959919055490596, 0.06390428654079872, 0.44428145800698543, 0.31862239078389015, 0.43615327365241185, 0.7446445961066632, 0.041128424063077415, 0.608351713664958, 0.4257855134362042, 0.31877296798586763, 0.4258503192298915, 0.907474545169143, 0.10101293743968566, 0.5742946814330231, 0.4717927469541086, 0.9297562617705418, 0.8084090072606311, 0.2005970624803512, 0.7859520469419587, 0.6914858424110555, 0.20398774477844323, 0.5356151107903748, 0.30528706911457076, 0.1064645608436006, 0.2657129604078149, 0.15777858983443055, 0.7498987884513197, 0.17220229878527987, 0.3521336310306631, 0.2844108452073026, 0.5520368957575471, 0.40557420572500025, 0.5880545645089051, 0.6166958594198579, 0.046225558392683753, 0.6669910328753789, 0.23902008017291274, 0.06789845965514749, 0.8514516203139133, 0.2534205956722542, 0.3801319622719964, 0.7208261216563393, 0.139128173997885, 0.6749994121963001, 0.7365126184943017, 0.24195822212189338, 0.8094359503984826, 0.29676583708841175, 0.670689878322204, 0.40137920017728296, 0.6559206512103943, 0.7357694118575434, 0.16128130595093204, 0.03966159382019955, 0.7907082357178336, 0.15930268817465204, 0.18743712436218474, 0.9384590447096008, 0.1986101450095638], [0.45444673944103287, 0.7440741014399523, 0.0504738190330339, 0.10983557494546303, 0.3628009503603485, 0.5403237520376832, 0.7201096705035778, 0.6056452924974852, 0.5620783035046029, 0.6602684098764394, 0.5389552169751405, 0.48417736820996776, 0.3449866135747634, 0.2332842701817156, 0.6247321245146612, 0.5109997902628981, 0.9496193265605287, 0.9964866826898079, 0.9893676589213071, 0.960898772451262, 0.45597715224680724, 0.06492079304052034, 0.6309293348797282, 0.32946839965533453, 0.5728576722675188, 0.4110391594431049, 0.6856259992784253, 0.9725080027420806, 0.2840061957772114, 0.8333028043504151, 0.8348854862024037, 0.3852860467356976, 0.6271349073749817, 0.5879801157486213, 0.4265515221680252, 0.8815454172702006, 0.8483361561831082, 0.8170586122703128, 0.4162187423784439, 0.3055952287361971, 0.6355300042108134, 0.4494871834010459, 0.4467466123278417, 0.7074260553142264, 0.4271776075212784, 0.41254200866970925, 0.19253880266005494, 0.7067889424831948, 0.632841509183578, 0.6977619611204428, 0.7173127255867913, 0.273734196370327, 0.4165832555915626, 0.821044306526635, 0.6964207941077745, 0.46974085572083196, 0.5461270731305123, 0.5796846016424323, 0.9491415989730193, 0.1686664300231378, 0.21504783585965936, 0.5266767495513618, 0.9172952135928363, 0.11039928468312803, 0.11754641388109922], [-0.6860639550611821, 0.5480763494342699, 0.7072032662897464, 0.016907111293858, 0.6462959373898156, 0.31531931044910166, -0.16612594729964217, -0.7013892397972225, -0.21014014587418367, -0.7093229167023481, 0.8159620912088791, 0.15946672291171632, 0.21252088008077058, 0.32036418033917846, -0.14322838393042348, 0.2739709385028623, 0.1000290817322003, 0.2371663084407447, -0.6697184079438708, 0.79991709399898, 0.00409981988528509, -0.8917705724518744, 0.19705159413839587, 0.5269676127723127, 0.16893649119725362, 0.36283245961459765, 0.13889183928682977, -0.446456140590195, -0.13510036744162282, 0.6756962883331324, 0.6975751427293647, 0.9090023420686247, 0.6248480550074444, 0.8156785048828047, 0.24848502666873137, -0.6336741883794229, -0.8174883529976559, 0.0004058440905739933, 0.5023354332294674, 0.6063880890167583, 0.784748348390544, 0.6686509307572553, -0.09562033097330117, 0.0918626519182782, 0.5747811881324902, -0.3981098013946185, 0.23373997998918372, 0.7855379797245959, 0.7678750024993966, -0.8451211437952576, 0.22683539746915446, 0.3003804540034184, 0.807593086963225, 0.4282938772617176, -0.7863375530133876, -0.07204860936173178, -0.6921607301686666, 0.5308454101150042, 0.6260233637410356, 0.9758602171592143, 0.9061093557414849, 0.45938297199232925, 0.5197532227378848, -0.7544063200387989, -0.4573305998879207], [0.6147813691567979, 0.930300486031464, 0.0636419248115776, 0.9342649338855629, 0.6644575051841233, 0.7532957681654264, 0.24346037896566, 0.8718603740713929, 0.7813217255725889, 0.8118933558883147, 0.24919952397649037, 0.0027768097899654102, 0.6811607861359291, 0.23804215493680383, 0.3191933065686864, 0.022205608992330785, 0.8224531606910739, 0.010401948830949397, 0.3218574361151446, 0.17713807193739584, 0.9480747861539247, 0.8578425629709164, 0.7873900889058257, 0.9148056268000033, 0.6163341131909538, 0.9424411361146178, 0.8491088227979621, 0.6179184339146144, 0.736033256864281, 0.44687125894493435, 0.3990006816245413, 0.0685669059944532, 0.8246108718751632, 0.5686740169894238, 0.32679861844607233, 0.7866219935733362, 0.22615267223664293, 0.5748303025441002, 0.9708266723847793, 0.7790769112369345, 0.7121530861240951, 0.8510353209727639, 0.7392275345945211, 0.11002586688541302, 0.7268793250471605, 0.2376236841481555, 0.9581030699726988, 0.3396016740682654, 0.784706785530541, 0.4328069187723661, 0.6380017841023606, 0.835884417491015, 0.9214893021355922, 0.51709048138024, 0.7822537335437866, 0.511912507546361, 0.1294331545762257, 0.18189297442492577, 0.4189929530676622, 0.3668911683797827, 0.8050100666545655, 0.8542429251981609, 0.4783829195612222, 0.3660767283952487, 0.05403594182999064], [0.5400632549550786, 0.4862096776986291, 0.859643339990881, 0.2855380807332854, 0.8450917685864329, 0.22061518094067578, 0.7523708529747563, 0.1765760346305692, 0.5015233663237783, 0.4896568246121078, 0.0938629898562155, 0.5635962475621312, 0.8814564337552222, 0.4342573755083555, 0.5043752247705258, 0.28508681980410083, 0.1145409738745437, 0.5038722319302213, 0.1942662508845267, 0.23159077183355742, 0.40250979314030244, 0.8615611029460096, 0.797041129254579, 0.1480944955217397, 0.4005415463009245, 0.749663254069623, 0.0136756299507707, 0.5093130810415727, 0.7608881472247799, 0.6598484798387674, 0.6328593371141725, 0.4840737109096243, 0.4482665514169654, 0.42290376476420594, 0.8102703207072152, 0.043553084641725366, 0.4159063494318685, 0.26821824020405194, 0.30467181622834294, 0.4113743645729519, 0.6029695538270486, 0.7927560539506133, 0.2523198311882611, 0.8124885198582276, 0.842494300410645, 0.8498995094403906, 0.17389858034330025, 0.5997538352122662, 0.3316144698790613, 0.8143746797870199, 0.27836889506217577, 0.6259664765286284, 0.8158436396781361, 0.08645981978619817, 0.054482440504033794, 0.8072334501738786, 0.360971151745241, 0.5120605991204679, 0.22460291641396807, 0.7684280116748169, 0.6074015959950999, 0.14019784806973534, 0.34691237346376735, 0.6239016353819609, 0.4035422665154177], [0.6820618496264775, 0.6323752280368791, 0.8691593796102892, 0.31670599010127887, 0.3877773369449059, 0.45848550420343626, 0.22759792968698073, 0.3910818917446155, 0.6938186237131164, 0.1073760236748386, 0.3304883386342419, 0.9041688671594716, 0.409196563741523, 0.8604634140725066, 0.4029512014431724, 0.5966291902537829, 0.8247146250064742, 0.24164523512995098, 0.2145608203704647, 0.6513107360146775, 0.9770795623709011, 0.9346968970919481, 0.33364623646757263, 0.49509523996785765, 0.6415345713161968, 0.9883656006324819, 0.8104783575505956, 0.11929601692944315, 0.41833342609162943, 0.4177945289596062, 0.6438328877667119, 0.12684217532222727, 0.6180981051778505, 0.21779796263809303, 0.13509894508823345, 0.44135224770661413, 0.42444990790661646, 0.07153072105834778, 0.06226095072863558, 0.5938284391560588, 0.15644147426113206, 0.32518877325664236, 0.09669176687760557, 0.6666121543638392, 0.5942872865889911, 0.39209256778606344, 0.394399002870166, 0.6091511088015237, 0.10314674853778347, 0.43260791239307345, 0.8882427512227417, 0.18225838929519234, 0.37480032092156645, 0.9583339899268443, 1.0683228301372267, 0.4014269519771127, 0.36039521902466276, 0.14589623922069386, 0.6996505591589147, 0.5868566014035106, 0.3404480453879746, 0.3386698455939292, 0.7238008206725353, 0.2789342272089085, 0.9893001982667922], [0.9162484419432041, 0.13388227552737234, 0.6389072098618066, 0.5622405356775912, 0.5875528276304102, 0.7080184554003159, 0.5851289659836488, 0.4457530441283822, 0.8729868783417173, 0.060791028436760756, 0.8187650330102707, 0.13600106442873514, 0.25082810312920367, 0.91923391716903, 0.28585297439246726, 0.6318759844021773, 0.5940283377178467, 0.3586818174334958, 0.8052156558916038, 0.6367686704115824, 0.0604411970726442, 0.35017279289802866, 0.16738664075165144, 0.3916689848266266, 0.9108843296829144, 0.3578457973212221, 0.9941014485259622, 0.7263936012876183, 0.3268892032865513, 0.2777121724715501, 0.5396039084542484, 0.6526943839609001, 0.11071933936173665, 0.6650719613630888, 0.20367469217565415, 0.3365568226960897, 0.9070119741962105, 0.6911270913157211, 0.6917901502182507, 0.05765618728191618, 0.36717680647281375, 0.6976956659341719, 0.0036884100296638894, 0.045572797844201283, 0.4225979526880999, 0.8180791761577015, 0.4927839672758181, 0.80853262670029, 0.9852666667291168, 0.9176195064046899, 0.37622660980046435, 0.353449583554797, 0.6385850930052973, 0.7678670189263626, 0.2643672784413931, 0.7587849600942277, 0.9454606255376979, 0.2686523028047072, 0.18072391723417472, 0.050260671286588225, 0.5785850930887982, 0.6360481196581316, 0.991781895923092, 0.6493257639501157, 0.4485916559399739]], [[0.46841286759119233, 0.13860886750413068, 0.43195495903170944, 0.2702346954427103, 1.0446243292871233, -10.435173556896684, 0.4256794508216349, 0.5412015411726352, 0.9107035694653091, 0.5012390045800265, 0.5319793573192844]]]
@jmss.mainloop
def Game():
    global pixels
    jmss.clear()

    if jmss.isKeyDown(KEY_SPACE):
        pixels = [0] * n * n

    mouse_pos = jmss.getMousePos()
    x = (mouse_pos[0] - border) // (side_length + margin)
    y = (mouse_pos[1] - border) // (side_length + margin)

    if jmss.isMousePressed(MOUSE_BUTTON_LEFT):
        if not(x < 0 or x >= n or y < 0 or y >= n):
            pixels[y * n + x] = 1

    if jmss.isKeyDown(KEY_X):
        print(str(pixels) + "," + str([1]))
    if jmss.isKeyDown(KEY_O):
        print(str(pixels) + "," + str([0]))

    if jmss.isKeyDown(KEY_ENTER):
        prediction = nn_predict(network,  pixels)[0]
        letter = "X" if prediction > 0.5 else "O"
        jmss.drawText("Prediction: " + letter +" , output: " + str(prediction), 0, 0, \
                      fontName = "Courier")
        
    for x in range(n):
        for y in range(n):
            jmss.drawRect(border + x * (side_length + margin), \
                          border + y * (side_length + margin), \
                          border + x * (side_length + margin) + side_length, \
                          border + y * (side_length + margin) + side_length, \
                          r = pixels[y * n + x], \
                          b = 1 - pixels[y * n + x], \
                          g = 0)
                            

jmss.run()