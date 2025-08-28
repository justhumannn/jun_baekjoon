# [Gold V] Hopscotch 50 - 18529 

[문제 링크](https://www.acmicpc.net/problem/18529) 

### 성능 요약

메모리: 33432 KB, 시간: 872 ms

### 분류

다이나믹 프로그래밍, 그래프 이론, 최단 경로, 데이크스트라

### 제출 일자

2025년 8월 28일 22:03:20

### 문제 설명

<p>There’s a new art installation in town, and it inspires you... to play a childish game. The art installation consists of a floor with an n×n matrix of square tiles. Each tile holds a single number from 1 to k. You want to play hopscotch on it. You want to start on some tile numbered 1, then hop to some tile numbered 2, then 3, and so on, until you reach some tile numbered k. You are a good hopper, so you can hop any required distance. You visit exactly one tile of each number from 1 to k.</p>

<p>What’s the shortest possible total distance over a complete game of Hopscotch? Use the Manhattan distance: the distance between the tile at (x<sub>1</sub>, y<sub>1</sub>) and the tile at (x<sub>2</sub>, y<sub>2</sub>) is |x<sub>1</sub> − x<sub>2</sub>| + |y<sub>1</sub> − y<sub>2</sub>|.</p>

### 입력 

 <p>The first line of input contains two space-separated integers n (1 ≤ n ≤ 50) and k (1 ≤ k ≤ n<sup>2</sup>), where the art installation consists of an n×n matrix with tiles having numbers from 1 to k.</p>

<p>Each of the next n lines contains n space-separated integers x (1 ≤ x ≤ k). This is the art installation.</p>

### 출력 

 <p>Output a single integer, which is the total length of the shortest path starting from some 1 tile and ending at some k tile, or −1 if it isn’t possible.</p>

