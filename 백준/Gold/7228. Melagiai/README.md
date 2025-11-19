# [Gold III] Melagiai - 7228 

[문제 링크](https://www.acmicpc.net/problem/7228) 

### 성능 요약

메모리: 37048 KB, 시간: 244 ms

### 분류

그래프 이론, 그래프 탐색, 강한 연결 요소, 이분 그래프, 2-sat

### 제출 일자

2025년 11월 20일 08:16:29

### 문제 설명

<p>Bitlandijoje netrukus prasidės Seimo rinkimai, o tai reiškia, kad nacionalinėje televizijoje „Bit TV“ vyksta politiniai debatai, kuriuose dalyvauja N kandidatų, ištraukusių numerius nuo 1 iki N. Kaip ir kasmet, Bronius šiuos debatus labai įdėmiai seka. Jis pastebėjo, kad šiais metais ypač dažnai kartojosi šie du scenarijai:</p>

<ul>
	<li>i-tasis kandidatas teigia, kad j-tasis kandidatas visada meluoja,</li>
	<li>i-tasis kandidatas teigia, kad j-tasis kandidatas visada sako tiesą.</li>
</ul>

<p>Visus tokius teiginius Bronius užsirašė ir dabar nori patikrinti, ar jie vienas kitam neprieštarauja.</p>

<p>Sakysime, kad teiginiai neprieštarauja vienas kitam, jei egzistuoja toks kandidatų paskirstymas į melagius ir nemelagius, kad visi melagių teiginiai būtų neteisingi, o visi nemelagių teiginiai būtų teisingi.</p>

<p>Padėkite Broniui nustatyti, ar toks kandidatų paskirstymas egzistuoja.</p>

### 입력 

 <p>Pirmoje eilutėje pateikti du sveikieji teigiami skaičiai – kandidatų skaičius N ir Broniaus surinktų teiginių skaičius M.</p>

<p>Toliau pateikta M eilučių. i-toje eilutėje pateikti i-tą teiginį apibūdinantys trys sveikieji skaičiai a<sub>i</sub>, b<sub>i</sub> ir m<sub>i</sub>:</p>

<ul>
	<li>Jei m<sub>i</sub> = 1, a<sub>i</sub>-tasis kandidatas teigė, kad b<sub>i</sub>-tasis kandidatas visada meluoja.</li>
	<li>Jei m<sub>i</sub> = 0, a<sub>i</sub>-tasis kandidatas teigė, kad b<sub>i</sub>-tasis kandidatas visada sako tiesą.</li>
</ul>

<p>(a<sub>i</sub>, b<sub>i</sub>) poros pradiniuose duomenyse yra unikalios, t. y., kandidatas a<sub>i</sub> gali pateikti tik vieną teiginį apie kandidatą b<sub>i</sub> arba visai jo nepateikti.</p>

### 출력 

 <p>Išveskite <code>EGZISTUOJA</code>, jei aprašytas paskirstymas į melagius ir nemelagius egzistuoja, arba <code>NEEGZISTUOJA</code>, jei neegzistuoja.</p>

