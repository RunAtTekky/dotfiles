package main

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
)

const USERNAME string = "runatme"

var API string = fmt.Sprintf("https://alfa-leetcode-api.onrender.com/%s/solved", USERNAME)

const FILENAME = ".lc_solved"

type Response struct {
	Problems_solved int `json:"solvedProblem"`
	Easy_solved     int `json:"easySolved"`
	Medium_solved   int `json:"mediumSolved"`
	Hard            int `json:"hardSolved"`
}

var response Response

func main() {

	home_directory, err := os.UserHomeDir()

	if err != nil {
		return
	}

	var FILEPATH = filepath.Join(home_directory, FILENAME)

	// Try reading from existing file
	ok, err := read_if_exists(FILEPATH)
	if ok && err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
		return
	}

	// Fetch
	resp, err := http.Get(API)
	if err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
		return
	}

	// Read the response
	body, err := io.ReadAll(resp.Body)
	defer resp.Body.Close()
	if err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
		return
	}

	// Store json data to response
	if err = json.Unmarshal(body, &response); err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
		return
	}

	fmt.Println(response.Problems_solved)

	// Write to file
	data := []byte(strconv.Itoa(response.Problems_solved))
	err = os.WriteFile(FILEPATH, data, 0644)
	if err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
		return
	}
}

func read_if_exists(filename string) (bool, error) {
	_, err := os.Stat(filename)

	if os.IsNotExist(err) {
		return false, err
	}

	data, err := ioutil.ReadFile(filename)

	if err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
		return true, err
	}

	response.Problems_solved, err = strconv.Atoi(string(data))

	if err != nil {
		fmt.Println(strconv.Itoa(response.Problems_solved))
	}

	return true, nil
}
