# [Gold I] Cantina of Babel - 11088 

[문제 링크](https://www.acmicpc.net/problem/11088) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

그래프 이론, 그래프 탐색, 강한 연결 요소

### 제출 일자

2025년 9월 19일 09:33:02

### 문제 설명

<p>Characters in Star Wars each speak a language, but they typically understand a lot more languages that they don’t or can’t speak. For example, Han Solo might speak in Galactic Basic and Chewbacca might respond in Shyriiwook; since they each understand the language spoken by the other, they can communicate just fine like this.</p>

<p>We’ll say two characters can converse if they can exchange messages in both directions. Even if they didn’t understand each other’s languages, two characters can still converse as long as there is a sequence of characters who could translate for them through a sequence of intermediate languages. For example, Jabba the Hutt and R2D2 might be able to converse with some help. Maybe when Jabba spoke in Huttese, Boba Fett could translate to Basic, which R2D2 understands. When R2D2 replies in Binary, maybe Luke could translate to Basic and then Bib Fortuna could translate back to Huttese for Jabba.</p>

<p>In Star Wars Episode IV, there’s a scene with a lot of different characters in a cantina, all speaking different languages. Some pairs of characters may not be able to converse (even if others in the cantina are willing to serve as translators). This can lead to all kinds of problems, fights, questions over who shot first, etc. You’re going to help by asking some of the patrons to leave. The cantina is a business, so you’d like to ask as few as possible to leave. You need to determine the size of the smallest set of characters S such that if all the characters in S leave, all pairs of remaining characters can converse.</p>

<p>For example, in the first sample input below, Chewbacca and Grakchawwaa can converse, but nobody else understands Shyriiwook, so they can’t converse with others in the bar. If they leave, everyone else can converse. In the second sample input, Fran and Ian can converse, as can Polly and Spencer, but no other pairs of characters can converse, so either everyone but Polly and Spencer must leave or everyone but Fran and Ian.</p>

### 입력 

 <p>Input starts with a positive integer, 1 ≤ N ≤ 100, the number of characters in the cantina. This is followed by N lines, each line describing a character. Each of these N lines starts with the character’s name (which is distinct), then the language that character speaks, then a list of 0 to 20 additional languages the character understands but doesn’t speak. All characters understand the language they speak. All character and language names are sequences of 1 to 15 letters (a-z and A-Z), numbers, and hyphens. Character names and languages are separated by single spaces.</p>

### 출력 

 <p>Print a line of output giving the size of the smallest set of characters S that should be asked to leave so that all remaining pairs of characters can converse.</p>

