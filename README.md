# Αρχιτεκτονική Προηγμένων Υπολογιστών - Εργαστήριο 3
## Εργαστήριο Β - Ομάδα 6
* Χατζηιορδάνου Ελισσάβετ 8269
* Πετρίδη Βασιλική 8602

### Βήμα 1

##### Ερώτημα 1

###### Επικύρωση του McPAT.

Η κύρια εστίαση του McPAT είναι η ακριβής μοντελοποίηση της ισχύος και της περιοχής, με βασικό περιορισμό τον χρονισμό. Η σχετική και η απόλυτη ακρίβεια είναι αμφότερες πολύ σημαντικές για την μοντελοποίηση ισχύος σε επίπεδο αρχιτεκτονικής. Σχετική ακρίβεια σημαίνει ότι οι αλλαγές στην μοντελοποιημένη ισχύ, ως αποτέλεσμα τροποποιήσεων στην αρχιτεκτονική, θα πρέπει να αντικατοπτρίζουν, σε σχετική κλίμακα, τις αλλαγές που θα βλέπαμε σε μια πραγματική σχεδίαση. Η απόλυτη ακρίβεια είναι εξίσου σημαντική αν θα θέλαμε να συγκρίνουμε τα αποτελέσματα με τα όρια θερμικής ισχύος σχεδιασμού (TDP) ή να βάλουμε την εξοικονόμιση ενέργειας στον πυρήνα στα πλαίσια ολόκληρου του επεξεργαστή ή όλου του συστήματος. Η σχετική ακρίβεια του McPAT εξασφαλίζει ότι τα σχετικά βάρη ισχύος των διαφορετικών στοιχείων ενός τσιπ έχουν μοντελοποιηθεί σωστά. Η απόλυτη ακρίβεια μεγέθους του McPAT σημαίνει ότι οι αριθμοί ισχύος για τα επιμέρους εξαρτήματα αλλά και η συνολική ισχύς αξιολογούνται σωστά. Για την επικύρωση του McPAT, έγινε σύγκριση των αποτελεσμάτων του  McPAT με δημοσιευμένα δεδομένα των εξής επεξεργαστών:
* __Niagara 90nm, 1.2 GHz, 1.2V__
* __Niagara2 65nm, 1.4GHz, 1.1V__
* __Xeon 65nm, 3.4GHz, 1.25V__
* __Alpha 21364 180nm, 1.2GHz, 1.5V__

Αυτά περιλαμβάνουν clock rates, working temperature, και παραμέτρους της αρχιτεκτονικής τους. Τα αποτελέσματα δείχνουν ότι οι αριθμοί ισχύος του μοντέλου ακολουθούν σε καλό βαθμό τους δημοσιευμένους αριθμούς των πραγματικών επεξεργαστών. 


##### Ερώτημα 2

* __Dynamic Power:__   Η δυναμική ισχύς είναι η ισχύς που χρειάζεται για την φόρτιση και αποφόρτιση των χωρητικών φορτίων για την αλλαγή της κατάστασης. Είναι ανάλογη με την συνολική χωρητικότητα φορτίου, την τάση τροφοδοσίας, την διακύμανση της τάσης κατά την μεταγωγή, την συχνότητα ρολογιού και τον συντελεστή δραστηριότητας. Δυναμική ισχυς καταναλώνεται μόνο όταν υπάρχει switching activity στο κύκλωμα.
* __Static Power or Leakage:__ Τα τρανζίστορ στα κυκλώματα έχουν διαρροές, με αποτέλεσμα να διαχέουν στατική ισχύ. Το ρεύμα διαρροής εξαρτάται από το πλάτος των τρανζίστορ και την τοπική κατάσταση των συσκευών. Υπάρχουν δύο μηχανισμοί διαρροής. Η διαρροή υποκατωφλίου, η οποία οφείλεται σε ενα μικρό ρεύμα που ρέει μεταξύ source και drain των τρανζίστορ που βρίσκονται σε off-state και η διαρροή πύλης, που είναι το ρεύμα που διαρρέει από τον ακροδέκτη της πύλης και διαφέρει σε μεγάλο βαθμό, ανάλογα με την κατάσταση της συσκευής.
* __Short-circuit Power:__ Η ισχύς βραχυκυκλώματος υπολογίζεται μέσω των εξισώσεων που προκύπτουν από το paper Nose et al που προβλέπει τάσεις για short-circuit power. Εαν ο λόγος threshold voltage/supply voltage συρρικνωθεί, η ισχύς βραχυκυκλώματος γίνεται πιο σημαντική. Συνήθως, είναι περίπου το 10% της συνολικής δυναμικής ισχύος, μπορεί όμως να φτάσει και το 25%.

Αυτό που θα επηρεαστεί είναι, προφανώς από τον ορισμό, το Dynamic Power καθώς για να τρέξουν τα προγράμματα χρειάζεται να γίνουν οι αντίστοιχες φορτίσεις και αποφορτίσεις των χωρητικών φορτίων. Τα υπόλοιπα, όπως φαίνεται από τους παραπάνω ορισμούς, δεν επηρεάζονται από το εκάστοτε πρόγραμμα αλλά από την αρχιτεκτονική. Όπως είδαμε, η δυναμική ισχύς δεν εξαρτάται από τον χρόνο εκτέλεσης οπότε το μέγεθος (σε χρονική διάρκεια) ενός προγράμματος δεν θα την επηρέαζε από μόνο του. Χρειαζόμαστε παραπάνω στοιχεία για το πρόγραμμα για μπορούμε να πούμε κατι τέτοιο με σιγουριά, όπως, για παράδειγμα, το switching frequency που ορίζει το πόσο συχνά θα γίνουν οι φορτίσεις και αποφορτίσεις των φορτίων.

##### Ερώτημα 3

Κάτι που θα πρέπει να λάβουμε υπόψην για να απαντήσουμε το παραπάνω ερώτημα είναι η ενεργειακή απόδοση. Στους υπολογιστές, το Performance per Watt είναι ένα μέτρο του energy efficiency μιας συγκεκριμένης αρχιτεκτονικής υπολογιστή. Ως performance, ορίζονται συχνά τα FLOPS (floating point operations per second) ή τα MIPS (instructions per second). Σύμφωνα με τα παραπάνω, ναι θα ήταν πιθανό ο δεύτερος επεξεργαστής που καταναλώνει 35 Watt να δίνει στο σύστημα μεγαλύτερη διάρκεια μπαταρίας από τον πρώτο που καταναλώνει 25 Watt. Δυστυχώς, ο McPAT δεν μπορεί να μας δώσει την σχετική απάντηση καθώς δεν μας δίνει κάποιο αποτέλεσμα για το performance, σε αντίθεση με τον gem5 που είχαμε εξετάσει στα προηγούμενα assignments.

##### Ερώτημα 4

Γνωρίζουμε από την εκφώνηση ότι ο Xeon μπορεί να τρέξει την ίδια εφαρμογη με τον Α9, 40 φορές γρηγορότερα. Έχουμε κάνει, επίσης, την υπόθεση ότι δεν διακόπτεται η λειτουργία  του συστήματος μετά την ολοκλήρωση εκτέλεσης της εφαρμογής. Παραθέτουμε, αρχικά, τα αποτελέσματα που πήραμε αφού τρέξαμε διαδοχικά τα παρακάτω:

```
./mcpat -infile ProcessorDescriptionFiles/Xeon.xml -print_level 5
```
και

```
./mcpat -infile ProcessorDescriptionFiles/ARM_A9_2GHz.xml -print_level 5
```
Για τον Xeon:

```
Total Leakage = 36.8319 W
Runtime Dynamic = 72.9199 W
```
Για τον ARM A9:

```
Total Leakage = 0.108687 W
Runtime Dynamic = 2.96053 W
```
Όπως αναφέραμε στο ερώτημα 3, η απόδοση από μόνη της δεν αρκεί για να κρίνουμε αν ένας επεξεργαστής έχει μεγαλύτερο energy efficiency από έναν άλλον. Παρατηρούμε ότι το Dynamic Power του Xeon είναι πολύ μεγαλύτερο από του Α9. Συνεπώς, αν χρησιμοποιήσουμε τον τύπο της απόδοσης, θα έχουμε τα εξής:
```
EnergyEfficiencyXeon = PerformanceX/PowerX= 40PerformanceA9/72.9199
EnergyEfficiencyA9 = PerformanceA9/PowerA9= PerformanceA9/2.96053
EnergyEfficiencyXeon/EnergyEfficiencyA9 = 0.55PerformanceA9/0.34PerformanceA9= 1.62
```
Όπως βλέπουμε, ο Xeon έχει περίπου 1.62 φορές καλύτερη απόδοση από τον Α9. Αυτό, ωστόσο, συμβαίνει μόνο όσο τρέχει το πρόγραμμα και χωρίς να λαμβάνουμε υπόψην την στατική ισχύ. Εφόσον δεν διακόπτεται η λειτουργία  του συστήματος μετά την ολοκλήρωση εκτέλεσης της εφαρμογής, θα πρέπει να λάβουμε υπόψην και το Leakage που πήραμε όταν χρησιμοποιήσαμε τον McPAT, το οποίο είναι περίπου 335 φορές μεγαλύτερο για τον Xeon απ' ότι για τον Α9. Κατά συνέπεια ο Xeon δεν θα μπορέσει να γίνει πιο energy efficient απο τον Α9 καθώς η διαφορά αυτού του μετρικού (Leakage) είναι αισθητά πιο κρίσιμη απο την διαφορά της απόδοσης . 


### Βήμα 2
##### Ερώτημα 1
Βασικό ζήτημα του βήματος 2 είναι η εξαγωγή του EDAP (Energy-Delay-Area Product) για κάθε μία απο τις προσομοιώσεις που δημιουργήθηκαν για το δεύτερο εργαστήριο, καθώς και η βελτιστοποίησή του. Για την επίτευξη του στόχου αυτού, χρησιμοποιώντας τα κατάλληλα [scripts](https://github.com/vasipetr/archlab3/tree/main/scripts), μετατρέπουμε τα αποτελέσματα του gem5, συγκεκριμένα τα αρχεία stats.txt και config.json, σε [xml αρχεία](https://github.com/vasipetr/archlab3/tree/main/xmls_gem5) και στη συνέχεια χρησιμοποιούμε τα αρχεία αυτά ως είσοδο για τον McPAT. Η [έξοδος του McPAT](https://github.com/vasipetr/archlab3/tree/main/mcpat_results) θα περιέχει πληροφορίες για τις παραμέτρους που χρειάζονται για τον υπολογισμό του EDAP. Πιο αναλυτικά για τις παραμέτρους που απαιτούνται:
* __Energy__: Η παράμετρος αυτή θα είναι ίση με το γινόμενο του Delay με το άθροισμα των Runtime Dynamic, Subthreshold Leakage και Gate Leakage στο Core και στην L2. (Μονάδα μέτρησης: mJ). Για πιο εύκολη εξαγωγή της ενέργειας, λόγω του μεγάλου αριθμού των προσομοιώσεων, γίνεται χρήση της συνάρτησης print_energy.py μέσα από το κατάλληλο script. Τα αποτελέσματα για το κάθε benchmark φαίνονται στο αρχείο [energy_results](https://github.com/vasipetr/archlab3/tree/main/energy_results).
* __Delay__: Είναι ίσο με το χρόνο εκτέλεσης κάθε προγράμματος και δίνεται από το sim_seconds, το οποίο μπορούμε να βρούμε στα stats.txt αρχεία του gem5. (Μονάδα μέτρησης: sec)
* __Area__: To άθροισμα της παραμέτρου Area στον Core και στην L2. (Μονάδα μέτρησης: mm^2)

##### Ερώτημα 2
Ακολουθούν τα διαγράμματα για τα benchmarks ως προς Area και Peak Power σύμφωνα με τις αλλαγές που έγιναν στις παραμέτρους στο προηγούμενο εργαστήριο:

![Figure_1](https://user-images.githubusercontent.com/73646657/150534128-f462ae40-f431-40cd-b33c-612401ed278b.png)
![Figure_2](https://user-images.githubusercontent.com/73646657/150534131-a2a10350-4ae4-4751-a816-5dd5b59d6ac2.png)
![Figure_3](https://user-images.githubusercontent.com/73646657/150534123-c258599d-1bbc-4e96-a4e4-32255c20337b.png)
![Figure_4](https://user-images.githubusercontent.com/73646657/150534124-331fa83a-7a15-4849-9b65-0ecb6a9ff5ae.png)
![Figure_5](https://user-images.githubusercontent.com/73646657/150534125-fc8028d5-f829-46d4-8524-acce8691a8cb.png)
![Figure_6](https://user-images.githubusercontent.com/73646657/150534127-4bab38b7-87a8-46df-be17-1edcba5dced6.png)

Σύμφωνα με τα αποτελέσματά μας, μπορούμε να πούμε ότι τα παραπάνω διαγράμματα αντικατοπτρίζουν τη συμπεριφορά όλων των benchmarks όσον αφορά Area και Peak Power.
##### Ερώτημα 3
Στο Βήμα 3 του προηγούμενου εργαστηρίου μας ζητήθηκε να κατασκευάσουμε μια συνάρτηση κόστους λαμβάνοντας υπόψιν τα αποτελέσματα των προσομοιώσεων. Καταλήξαμε στη συνάρτηση κόστους:
```
Cost = 0.4(L1isize + L1dsize) + 0.3(L1iassoc + L1dassoc) + 0.15(L2size) + 0.1(L2assoc) + 0.05(cache line size)
```
με τη λογική ότι:

*	**Βαρύτητα α:** Το μέγεθος την μνήμης cache L1 είναι αυτό με το μεγαλύτερο κόστος σε σχέση με τα άλλα στοιχεία. Γι'αυτό και το βάρος που το αντιπροσωπεύει θα πρέπει σχεδόν να ισούται με το άθροισμα των υπολοίπων.
*	**Βαρύτητα β:** Αύξηση του associativity αυξάνει την πολυπλοκότητα και αντίστοιχα το κόστος. Συγκεκριμένα για το associativity της L1, η βαρύτητα του στην συνάρτηση κόστους μας θα είναι μεγάλη, σχεδόν αντίστοιχη της βαρύτητας α.
*	**Βαρύτητα γ και βαρύτητα δ:** Το μέγεθος της μνήμης L2 αν και σημαντικό για την λειτουργία της CPU μας είναι αρκετά μικρότερο από αυτό της L1. Θα ισχύει το αντίστοιχο για το associativity της. Γι αυτό και αυτά τα δύο βάρη θα αντιπροσωπεύουν περίπου το 1/4 του αθροίσματος όλων των βαρών.
*	**Βαρύτητα ε:** Το μέγεθος της cache line size επηρεάζει το κόστος λιγότερο από όλα τα υπόλοιπα στοιχεία και για αυτό θα έχει την αντίστοιχη βαρύτητα, η οποία θα είναι της τάξης του 5%.

Σύμφωνα με τα διαγράμματα του προηγούμενου ερωτήματος βλέπουμε ότι σημαντική αύξηση υπάρχει στο Area του Core και L2 όταν μεταβάλλονται οι σχετικοί παράγοντες και υπάρχει, επίσης, μια σχετική αύξηση σε μικρότερο βαθμό στη μέγιστη κατανάλωση ισχύος (peak power). Οι παράγοντες που επηρέσαν τη συνάρτηση κόστους φαίνεται να είναι οι ίδιοι που επηρεάζουν το Area κai Peak Power, δηλ. Cache Line Size, L1 Dcache,Icache και L1 Associativity, καθώς και το μέγεθος της L2 στην περίπτωση του Area. Απ' ότι φαίνεται οι αλλαγές που οδηγούν σε καλύτερο performance είναι και αυτές που "κοστίζουν" περισσότερο σε ισχύ.
## Κριτική:
Όσον αφορά το πρώτο βήμα της εργασίας, μας έδωσε την ευκαιρία να μάθουμε πολλά καινούργια πράγματα για τους επεξεργαστές και για τον McPAT. Αυτό που βρήκαμε επίσης πολύ χρήσιμο ήταν η εξοικείωση με την μελέτη και την εξαγωγή πληροφοριών από ένα επιστημονικό paper. Εξοικειωθήκαμε ακόμα περισσότερο με την αυτοματοποίηση των διαδικασιών, καθώς χρειάστηκαν αρκετά bash scripts για πιο γρήγορη υλοποίηση των ερωτημάτων, αλλά και με την οπτικοποίηση των αποτελεσμάτων μας μέσω διαγραμμάτων.
## Συνολική Κριτική για τα Εργαστήρια:
Οι εργασίες στο σύνολό τους είχαν μεγάλο ενδιαφέρον. Η δυσκολία, σχετικά με το πρακτικό κομμάτι τους, προερχόταν περισσότερο από το γεγονός ότι ήταν χρονοβόρες, παρά δύσκολες στην εκπόνησή τους. Επίσης, η δυσκολία αυτή είχε κλιμάκωση από την πρώτη έως την τρίτη, καθώς με κάθε κομμάτι εμβαθύναμε όλο και περισσότερο στο αντικείμενο. Μπορούμε να πούμε με σιγουριά ότι μέσω της εργασίας αυξήθηκαν οι θεωρητικές μας γνώσεις πάνω στο αντικείμενο του μαθήματος, καθώς κάθε μέρος απαιτούσε να ανατρέξουμε σε πηγές που δε μας δίνονταν στην εκφώνηση και πολλές φορές βρεθήκαμε να συνεχίζουμε την αναζήτηση ακόμα και μετά το πέρας του κάθε μέρους, επειδή το αντικείμενο μάς κίνησε το ενδιαφέρον. Για το μέλλον, σίγουρα ακόμα και αν δεν ασχοληθούμε με το αντικείμενο, έχουμε την επιθυμία να συνεχίσουμε να ενημερωνόμαστε για τις εξελίξεις του.

Πηγές: [https://www.hpl.hp.com/research/mcpat/McPATAlpha_TechRep.pdf], [https://www.hpl.hp.com/research/mcpat/micro09.pdf], [https://www.sciencedirect.com/topics/computer-science/dynamic-power-dissipation], [https://en.wikipedia.org/wiki/Performance_per_watt]
