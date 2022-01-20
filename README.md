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
Βασικό ζήτημα του βήματος 2 είναι η εξαγωγή του EDAP (Energy-Delay-Area Product) για κάθε μία απο τις προσομοιώσεις που δημιουργήθηκαν για το δεύτερο εργαστήριο. Με τη χρήση των κατάλληλων [scripts](https://github.com/vasipetr/archlab3/tree/main/scripts) μετατρέπουμε τα αποτελέσματα του gem5 σε [xml αρχεία](https://github.com/vasipetr/archlab3/tree/main/xmls_gem5) και στη συνέχεια χρησιμοποιούμε τα αρχεία αυτά ως είσοδο για τον McPAT. Η [έξοδος του McPAT](https://github.com/vasipetr/archlab3/tree/main/mcpat_results) θα περιέχει πληροφορίες για τις παραμέτρους που χρειάζονται για τον υπολογισμό του EDAP. Πιο αναλυτικά για τις παραμέτρους που απαιτούνται:
* Energy: 

## Κριτική:
Όσον αφορά το πρώτο βήμα της εργασίας, μας έδωσε την ευκαιρία να μάθουμε πολλά καινούργια πράγματα για τους επεξεργαστές και για τον McPAT. Αυτό που βρήκαμε επίσης πολύ χρήσιμο ήταν η εξοικείωση με την μελέτη και την εξαγωγή πληροφοριών από ένα επιστημονικό paper .

Πηγές: [https://www.hpl.hp.com/research/mcpat/McPATAlpha_TechRep.pdf], [https://www.hpl.hp.com/research/mcpat/micro09.pdf], [https://www.sciencedirect.com/topics/computer-science/dynamic-power-dissipation], [https://en.wikipedia.org/wiki/Performance_per_watt]
