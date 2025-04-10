package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
)

const USERNAME = "RunAt"

var API = fmt.Sprintf("https://codeforces.com/api/user.status?handle=%s", USERNAME)

var RATINGS = []int{
	800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700,
	1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700,
	2800, 2900, 3000,
}

type Problem struct {
	Index  string `json:"index"`
	Rating int    `json:"rating"`
}

type Result struct {
	ContestID int     `json:"contestId"`
	Problem   Problem `json:"problem"`
	Verdict   string  `json:"verdict"`
}

type Response struct {
	Status  string   `json:"status"`
	Results []Result `json:"result"`
}

var response Response

const FILENAME = ".cf_result"

var FILEPATH string

var data []byte

func main() {
	// Create PATH
	HOME_DIR, err := os.UserHomeDir()
	if err != nil {
		return
	}
	FILEPATH = filepath.Join(HOME_DIR, FILENAME)

	// Read from file if exists
	ok, err := read_if_exists()

	if ok && err != nil {
		return
	}

	fetch_data()

	err = json.Unmarshal(data, &response)
	if err != nil {
		// fmt.Println("Error converting json")
		return
	}

	problemID_map := make(map[string]bool)
	count_map := make(map[int]int)

	get_count(problemID_map, count_map)

	rating_arg := os.Args[1]

	rating, err := strconv.Atoi(rating_arg)

	if err != nil {
		return
	}

	fmt.Println(count_map[rating])

	err = os.WriteFile(FILEPATH, data, 0644)
	if err != nil {
		// fmt.Println("Error writing to file")
		return
	}

}

func read_if_exists() (bool, error) {

	_, err := os.Stat(FILEPATH)
	if err != nil {
		return false, err
	}

	dataf, err := os.ReadFile(FILEPATH)
	if err != nil {
		return true, err
	}

	data = dataf
	// fmt.Println(string(dataf))

	return true, nil
}

func get_count(problemID_map map[string]bool, count_map map[int]int) {
	for _, result := range response.Results {
		if result.Verdict != "OK" {
			continue
		}

		problemID := strconv.Itoa(result.ContestID) + result.Problem.Index
		if _, ok := problemID_map[problemID]; ok {
			continue
		}
		problemID_map[problemID] = true

		count_map[result.Problem.Rating]++
	}
}

func fetch_data() bool {
	resp, err := http.Get(API)

	if err != nil {
		// fmt.Println("Error getting response")
		return false
	}

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		// fmt.Println("Error reading response")
		return false
	}

	data = body

	return true
}
