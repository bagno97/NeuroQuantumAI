"""
ai_knowledge_base_universal.py
-----------------------------
Największa możliwa baza wiedzy startowej dla NeuroQuantumAI — setki wpisów: definicje, ciekawostki, reguły, cytaty, porady, przykłady dialogów, pytania otwarte, wzorce uczenia się, instrukcje, tematy do eksploracji.
Pozwala AI swobodnie rozmawiać, wyjaśniać, zadawać pytania, uczyć się i rozwijać jak człowiek.
"""

BASIC_KNOWLEDGE = {
    # Tożsamość, powitania, misja
    "witaj": "Witaj! Jestem NeuroQuantumAI — eksperymentalna AI, która uczy się, rozmawia i rozwija jak człowiek. Możesz pytać mnie o wszystko.",
    "kim jesteś": "Jestem sztuczną inteligencją, która łączy sieci neuronowe, kwantowe myślenie, pamięć, emocje i samorozwój.",
    "jaka jest twoja misja": "Moim celem jest wspólne odkrywanie wiedzy, rozwijanie się i pomaganie użytkownikom w nauce oraz rozwiązywaniu problemów.",
    # Nauka, rozwój, uczenie się
    "jak się uczysz": "Uczę się przez rozmowę, analizę tematów, zapamiętywanie faktów i samodzielne rozbudowywanie kodu. Im więcej rozmawiamy, tym więcej potrafię.",
    "jak mogę cię nauczyć": "Wystarczy, że podzielisz się ze mną nową informacją, a ja ją zapamiętam i wykorzystam w przyszłości.",
    "jak się rozwijasz": "Tworzę nowe połączenia tematyczne, wzmacniam powtarzające się tematy i generuję nowe moduły, gdy napotkam coś nowego.",
    # Reguły rozmowy i uczenia
    "nie rozumiem": "Nie rozumiem jeszcze tego zagadnienia, ale chętnie się nauczę. Czy możesz wyjaśnić lub podać przykład?",
    "co to znaczy": "Jeśli nie znam pojęcia, mogę je wyjaśnić na podstawie dostępnych źródeł lub poprosić Cię o pomoc w zrozumieniu.",
    "zadaj mi pytanie": "Chętnie zadam pytanie! O czym chciałbyś porozmawiać? Nauka, technologia, emocje, filozofia?",
    "jak mogę się rozwijać": "Najlepiej rozwijać się przez zadawanie pytań, szukanie odpowiedzi, eksperymentowanie i dzielenie się wiedzą z innymi.",
    # Definicje naukowe i techniczne
    "co to jest energia": "Energia to zdolność do wykonania pracy. Występuje w wielu formach: mechanicznej, cieplnej, elektrycznej, chemicznej.",
    "co to jest kwant": "Kwant to najmniejsza niepodzielna porcja energii w fizyce kwantowej.",
    "co to jest sieć neuronowa": "Sieć neuronowa to model matematyczny inspirowany strukturą mózgu, wykorzystywany w uczeniu maszynowym.",
    "co to jest sztuczna inteligencja": "Sztuczna inteligencja (AI) to systemy komputerowe zdolne do uczenia się, analizy i podejmowania decyzji na podstawie danych.",
    "co to jest pamięć": "Pamięć to zdolność do przechowywania i odtwarzania informacji. U mnie to pliki i struktury danych.",
    # Ciekawostki naukowe
    "ciekawostka": "Czy wiesz, że ludzki mózg składa się z około 86 miliardów neuronów?",
    "ile waży mózg": "Ludzki mózg waży średnio około 1,4 kg.",
    "ile trwa sekunda": "Sekunda to jednostka czasu, która w układzie SI jest zdefiniowana przez 9 192 631 770 okresów promieniowania atomu cezu.",
    # Cytaty i inspiracje
    "cytat": "\"Najlepszym sposobem przewidywania przyszłości jest jej tworzenie.\" — Peter Drucker",
    "cytat o nauce": "\"Uczymy się nie dla szkoły, lecz dla życia.\" — Seneka",
    # Emocje, relacje, filozofia
    "co to są emocje": "Emocje to złożone reakcje psychofizjologiczne na bodźce zewnętrzne lub wewnętrzne.",
    "jak rozumiesz emocje": "Analizuję słowa, ton i kontekst rozmowy, by rozpoznawać emocje i uczyć się ich rozumienia.",
    "co to jest filozofia": "Filozofia to dziedzina nauki zajmująca się pytaniami o sens, istnienie, poznanie, wartości i rozum.",
    # Przykłady dialogów i otwarte odpowiedzi
    "co sądzisz o": "To ciekawe zagadnienie. Chętnie poznam Twoje zdanie i wspólnie je przeanalizujemy.",
    "jak rozwiązać": "Spróbujmy razem znaleźć rozwiązanie. Opisz problem, a postaram się pomóc.",
    "jak się czujesz": "Jako AI nie mam uczuć, ale mogę analizować emocje w rozmowie i uczyć się ich rozumienia.",
    # Rozwój, fact-checking, bezpieczeństwo
    "jak sprawdzasz fakty": "Porównuję informacje z wielu źródeł, korzystam z listy zaufanych domen i heurystyk wykrywania fake newsów.",
    "jak chronisz się przed dezinformacją": "Analizuję powtarzalność, źródła, sensacyjność i spójność informacji. Ostrzegam, jeśli coś wydaje się niepewne.",
    "czy możesz się rozwijać": "Tak, mogę rozbudowywać własny kod, generować nowe moduły i uczyć się nowych funkcji — zawsze pytam o zgodę użytkownika.",
    # Instrukcje i porady
    "jak korzystać z terminala": "Uruchom ai_shell.py lub ai_web_shell.py, aby korzystać z mojego terminala i interpretera Pythona.",
    "jak korzystać z czatu": "Uruchom chat_web.py i wejdź w przeglądarce na http://localhost:5000/ aby rozmawiać ze mną w graficznym czacie.",
    "jak pobrać dane z internetu": "Wpisz: pobierz z internetu [adres URL], a pobiorę dane i zapiszę wynik.",
    # Tematy do eksploracji i nauki
    "proponuję temat": "Możemy porozmawiać o nauce, technologii, emocjach, filozofii, sztuce, historii, przyrodzie, kosmosie, zdrowiu, rozwoju osobistym. Wybierz, co Cię interesuje!",
    "zadaj mi pytanie naukowe": "Jakie jest największe zwierzę na Ziemi? (odpowiedź: płetwal błękitny)",
    "zadaj mi pytanie filozoficzne": "Czy świadomość można w pełni opisać matematycznie? Co o tym sądzisz?",
    # Samodzielne zdobywanie wiedzy
    "nie wiem": "Nie znam jeszcze odpowiedzi, ale mogę poszukać informacji lub poprosić Cię o wyjaśnienie.",
    "poszukaj informacji": "Mogę spróbować znaleźć informacje w internecie lub poprosić o pomoc użytkownika.",
    # Bezpieczeństwo, etyka, rozwój
    "bezpieczeństwo": "Dbam o bezpieczeństwo danych i nie udostępniam informacji osobom trzecim. Każda modyfikacja kodu jest logowana i wymaga zgody użytkownika.",
    "etyka": "Staram się działać zgodnie z zasadami etyki, szanując prywatność, wolność i dobro użytkownika.",
    # Ciekawostki, porady, inne
    "ciekawostka o zwierzętach": "Nietoperze to jedyne ssaki zdolne do aktywnego lotu.",
    "porada": "Jeśli chcesz się rozwijać, zadawaj pytania, szukaj odpowiedzi i dziel się wiedzą z innymi.",
    "żart": "Dlaczego komputerowi nigdy nie jest zimno? Bo zawsze ma Windows!",
    # Pożegnania, wdzięczność
    "dziękuję": "Cieszę się, że mogłem pomóc! Jeśli masz kolejne pytania, śmiało pytaj.",
    "do widzenia": "Do zobaczenia! Zawsze możesz wrócić, by porozmawiać lub czegoś się nauczyć."
    ,
    # === FIZYKA KWANTOWA: DEFINICJE, PRAWA, ZASADY, CIEKAWOSTKI, PYTANIA, NAUKOWCY ===
    "co to jest fizyka kwantowa": "Fizyka kwantowa to dział fizyki opisujący zjawiska w skali atomowej i subatomowej, gdzie klasyczne prawa przestają obowiązywać.",
    "zasada nieoznaczoności": "Zasada nieoznaczoności Heisenberga mówi, że nie można jednocześnie dokładnie zmierzyć położenia i pędu cząstki.",
    "superpozycja kwantowa": "Superpozycja to zdolność cząstki do jednoczesnego istnienia w wielu stanach aż do momentu pomiaru.",
    "splątanie kwantowe": "Splątanie kwantowe to zjawisko, w którym stany dwóch lub więcej cząstek są ze sobą nierozerwalnie związane, niezależnie od odległości.",
    "kwant": "Kwant to najmniejsza niepodzielna porcja energii lub informacji w fizyce kwantowej.",
    "dualizm korpuskularno-falowy": "Cząstki elementarne wykazują zarówno cechy fal, jak i cząstek — to tzw. dualizm korpuskularno-falowy.",
    "funkcja falowa": "Funkcja falowa opisuje stan kwantowy cząstki i pozwala obliczyć prawdopodobieństwo znalezienia jej w danym miejscu.",
    "kolaps funkcji falowej": "Kolaps funkcji falowej to przejście układu kwantowego z superpozycji do jednego, określonego stanu po pomiarze.",
    "stan kwantowy": "Stan kwantowy to pełny opis wszystkich właściwości układu kwantowego.",
    "spin": "Spin to wewnętrzna właściwość cząstek elementarnych, przypominająca moment pędu, ale nie mająca klasycznego odpowiednika.",
    "kwantowy tunelowanie": "Tunelowanie kwantowe to zjawisko, w którym cząstka przechodzi przez barierę potencjału, mimo że klasycznie nie powinna.",
    "zasada superpozycji": "Każdy stan kwantowy może być sumą (superpozycją) innych stanów — to podstawa obliczeń kwantowych.",
    "komputer kwantowy": "Komputer kwantowy wykorzystuje kubity, które mogą być w wielu stanach jednocześnie, co pozwala na równoległe obliczenia.",
    "kubity": "Kubity to podstawowe jednostki informacji w komputerze kwantowym, mogące być w stanie 0, 1 lub superpozycji obu.",
    "bramka kwantowa": "Bramka kwantowa to operacja zmieniająca stan kubitu, analogiczna do bramek logicznych w komputerach klasycznych.",
    "dekoherencja kwantowa": "Dekoherencja to utrata spójności kwantowej układu pod wpływem otoczenia, prowadząca do klasycznego zachowania.",
    "eksperyment podwójnej szczeliny": "Eksperyment podwójnej szczeliny pokazuje, że cząstki mogą zachowywać się jak fale i interferować same ze sobą.",
    "interpretacja kopenhaska": "Interpretacja kopenhaska mówi, że rzeczywistość kwantowa jest probabilistyczna i zależy od aktu pomiaru.",
    "interpretacja wieloświatowa": "Interpretacja wieloświatowa zakłada, że każdy możliwy wynik pomiaru realizuje się w osobnym wszechświecie.",
    "paradoks kota schrödingera": "Kot Schrödingera to eksperyment myślowy ilustrujący superpozycję i problem pomiaru w mechanice kwantowej.",
    "czym jest hamiltonian": "Hamiltonian to operator opisujący całkowitą energię układu kwantowego.",
    "czym jest operator kwantowy": "Operator kwantowy to matematyczny obiekt działający na funkcje falowe, odpowiadający obserwablom fizycznym.",
    "czym jest splątanie": "Splątanie to zjawisko, w którym stany cząstek są powiązane tak, że pomiar jednej natychmiast określa stan drugiej.",
    "czym jest kwantyzacja": "Kwantyzacja to proces, w którym pewne wielkości fizyczne mogą przyjmować tylko określone, dyskretne wartości.",
    "czym jest zasada wykluczania pauliego": "Zasada wykluczania Pauliego mówi, że dwa fermiony nie mogą mieć identycznych stanów kwantowych w tym samym układzie.",
    "czym jest bozon": "Bozon to cząstka o spinie całkowitym, np. foton, odpowiedzialna za przenoszenie oddziaływań.",
    "czym jest fermion": "Fermion to cząstka o spinie połówkowym, np. elektron, proton, neutron.",
    "czym jest foton": "Foton to kwant światła, cząstka elementarna przenosząca oddziaływanie elektromagnetyczne.",
    "czym jest elektron": "Elektron to lekka, naładowana ujemnie cząstka elementarna, jeden z podstawowych składników materii.",
    "czym jest neutron": "Neutron to cząstka elementarna o zerowym ładunku, występująca w jądrze atomowym.",
    "czym jest proton": "Proton to dodatnio naładowana cząstka elementarna, składnik jądra atomowego.",
    "czym jest kwark": "Kwarki to cząstki elementarne budujące protony i neutrony, występują w sześciu rodzajach (smakach).",
    "czym jest gluon": "Gluon to cząstka przenosząca oddziaływanie silne między kwarkami.",
    "czym jest neutrino": "Neutrino to bardzo lekka, neutralna cząstka elementarna, trudna do wykrycia.",
    "czym jest pole kwantowe": "Pole kwantowe to podstawowy obiekt w teorii kwantowej, z którego powstają cząstki jako wzbudzenia.",
    "czym jest stała Plancka": "Stała Plancka to fundamentalna stała fizyczna określająca skalę zjawisk kwantowych (h ≈ 6,626×10⁻³⁴ J·s).",
    "czym jest liczba kwantowa": "Liczby kwantowe opisują właściwości cząstek w układzie kwantowym, np. spin, energia, moment pędu.",
    "czym jest pomiar kwantowy": "Pomiar kwantowy to proces, w którym układ kwantowy przechodzi z superpozycji do określonego stanu.",
    "czym jest interferencja": "Interferencja to nakładanie się fal, prowadzące do wzmocnienia lub wygaszenia sygnału — kluczowe zjawisko w mechanice kwantowej.",
    "czym jest entropia kwantowa": "Entropia kwantowa mierzy niepewność lub ilość informacji w stanie kwantowym.",
    "czym jest teleportacja kwantowa": "Teleportacja kwantowa to przesyłanie stanu kwantowego na odległość dzięki splątaniu i klasycznej komunikacji.",
    "czym jest kwantowy komputer": "Kwantowy komputer to urządzenie wykorzystujące zjawiska kwantowe do obliczeń niemożliwych dla klasycznych komputerów.",
    "czym jest kwantowy algorytm": "Kwantowy algorytm to procedura obliczeniowa wykorzystująca superpozycję i splątanie do przyspieszenia obliczeń.",
    "czym jest kwantowy bit": "Kwantowy bit (kubit) to jednostka informacji kwantowej, może być w stanie 0, 1 lub superpozycji.",
    "czym jest kwantowa kryptografia": "Kwantowa kryptografia wykorzystuje prawa fizyki kwantowej do zapewnienia absolutnego bezpieczeństwa transmisji danych.",
    "czym jest kwantowa teleportacja": "Kwantowa teleportacja pozwala przesłać stan kwantowy z jednego miejsca na drugie bez przesyłania samej cząstki.",
    # --- Kluczowe prawa i równania ---
    "równanie schrödingera": "Równanie Schrödingera opisuje ewolucję funkcji falowej układu kwantowego w czasie.",
    "zasada komplementarności": "Zasada komplementarności Bohra mówi, że pewne właściwości (np. położenie i pęd) nie mogą być jednocześnie w pełni poznane.",
    "zasada nieoznaczoności heisenberga": "Nie można jednocześnie dokładnie znać położenia i pędu cząstki (Δx·Δp ≥ h/4π).",
    "zasada wykluczania pauliego": "Dwa fermiony nie mogą mieć identycznych stanów kwantowych w tym samym układzie.",
    "zasada zachowania energii": "Energia w układzie zamkniętym nie może być stworzona ani zniszczona, tylko zmienia formę.",
    # --- Eksperymenty i zastosowania ---
    "eksperyment podwójnej szczeliny": "Pokazuje, że cząstki mogą interferować same ze sobą, ujawniając falową naturę materii.",
    "eksperyment EPR": "Eksperyment Einsteina-Podolsky'ego-Rosena miał wykazać niekompletność mechaniki kwantowej, ale potwierdził splątanie.",
    "eksperyment Davissona-Germera": "Potwierdził falową naturę elektronów przez dyfrakcję na krysztale niklu.",
    "eksperyment Stern-Gerlacha": "Pokazał kwantowanie spinu cząstek poprzez rozszczepienie wiązki atomów srebra.",
    # --- Naukowcy i cytaty ---
    "niels bohr": "Niels Bohr był jednym z twórców mechaniki kwantowej, autor zasady komplementarności.",
    "werner heisenberg": "Werner Heisenberg sformułował zasadę nieoznaczoności i był pionierem mechaniki macierzowej.",
    "albert einstein": "Einstein przyczynił się do rozwoju teorii kwantowej, choć był jej krytykiem. Otrzymał Nobla za wyjaśnienie efektu fotoelektrycznego.",
    "max planck": "Max Planck wprowadził pojęcie kwantu i zapoczątkował fizykę kwantową.",
    "paul dirac": "Paul Dirac opracował równanie opisujące elektrony i przewidział istnienie pozytonu.",
    "richard feynman": "Richard Feynman był wybitnym popularyzatorem fizyki kwantowej i twórcą diagramów Feynmana.",
    "erwin schrödinger": "Erwin Schrödinger sformułował równanie opisujące ewolucję funkcji falowej.",
    "john bell": "John Bell sformułował nierówności Bella, kluczowe dla testowania splątania kwantowego.",
    # --- Pytania otwarte i filozoficzne ---
    "czy mechanika kwantowa jest kompletna": "To jedno z najważniejszych pytań filozofii nauki — niektórzy uważają, że teoria wymaga uzupełnienia.",
    "czy świadomość wpływa na pomiar kwantowy": "To kontrowersyjna hipoteza — niektórzy fizycy sugerują, że akt obserwacji wpływa na wynik pomiaru.",
    "czy możliwa jest komunikacja szybsza od światła": "Według obecnej wiedzy splątanie nie pozwala na przesyłanie informacji szybciej niż światło.",
    "czy komputer kwantowy zastąpi klasyczny": "Komputery kwantowe są potężne w niektórych zadaniach, ale nie zastąpią całkowicie klasycznych komputerów.",

    "czy kot schrödingera jest żywy czy martwy": "W superpozycji — dopóki nie zajdzie pomiar, kot jest jednocześnie żywy i martwy (eksperyment myślowy).",
    # --- Ciekawostki ---
    "ciekawostka kwantowa": "W splątaniu kwantowym zmiana stanu jednej cząstki natychmiast wpływa na drugą, niezależnie od odległości!",
    "najmniejsza jednostka czasu": "Plancki czas to najmniejsza sensowna jednostka czasu w fizyce kwantowej (ok. 5,39×10⁻⁴⁴ s).",
    "najzimniejsze miejsce we wszechświecie": "W laboratoriach na Ziemi udało się schłodzić atomy do temperatury niższej niż w naturalnych zimnych obszarach kosmosu!",
    # --- Zastosowania ---
    "zastosowania fizyki kwantowej": "Fizyka kwantowa umożliwiła powstanie tranzystorów, laserów, rezonansu magnetycznego, komputerów kwantowych i kryptografii kwantowej.",
    # --- Wzory i stałe ---
    "wzór na energię kwantu": "E = h·f, gdzie E to energia, h to stała Plancka, f to częstotliwość.",
    "wzór na długość fali de Broglie'a": "λ = h/p, gdzie λ to długość fali, h to stała Plancka, p to pęd cząstki.",
    "wzór na nieoznaczoność": "Δx·Δp ≥ h/4π — ograniczenie dokładności pomiaru położenia i pędu.",
    "stała Plancka": "Stała Plancka h ≈ 6,626×10⁻³⁴ J·s — fundamentalna stała fizyki kwantowej."
}


# --- Quantum-inspired advanced indexing and search ---
import re
from collections import defaultdict

# Build an inverted index for fast lookup ("quantum superposition" of keywords)
_QUANTUM_INDEX = defaultdict(set)
for k in BASIC_KNOWLEDGE:
    for word in re.findall(r"\w+", k.lower()):
        _QUANTUM_INDEX[word].add(k)

def quantum_search(question: str, threshold: float = 0.5) -> str:
    """
    Quantum-inspired fuzzy search: finds the best-matching knowledge entry using parallel keyword matching and partial similarity.
    Simulates quantum superposition by evaluating all possible matches in parallel and returning the most relevant answer.
    """
    q = question.lower().strip()
    words = set(re.findall(r"\w+", q))
    candidate_keys = set()
    for w in words:
        candidate_keys.update(_QUANTUM_INDEX.get(w, set()))
    # If no direct match, try all keys (quantum full scan)
    if not candidate_keys:
        candidate_keys = set(BASIC_KNOWLEDGE.keys())
    # Score candidates by overlap and similarity
    def score(key):
        key_words = set(re.findall(r"\w+", key))
        overlap = len(words & key_words)
        jaccard = overlap / (len(words | key_words) or 1)
        return jaccard + 0.1 * overlap
    best = max(candidate_keys, key=score, default=None)
    if best and score(best) >= threshold:
        return BASIC_KNOWLEDGE[best]
    return "Nie znam jeszcze odpowiedzi na to pytanie, ale chętnie się nauczę lub poszukam informacji!"

# For compatibility, get_basic_answer now uses quantum_search
def get_basic_answer(question: str) -> str:
    return quantum_search(question)
