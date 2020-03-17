package zvmconnector

import (
	"net/http"
	"os"
	"strconv"
	"time"
)

// RestClient use the sdk api
type RestClient struct {
	connect   *http.Client
	URL       string
	authToken string
}

// NewRestClient create a RestClient
func NewRestClient(ip string, port uint16, timeout time.Duration, tokenPath string) (*RestClient, error) {
	serverAddr := ip + ":" + strconv.Itoa(int(port))
	httpClient := &http.Client{}
	httpClient.Timeout = timeout

	c := &RestClient{
		connect: httpClient,
		URL:     serverAddr,
	}
	return c, nil
}

// Fetch the data
func (client *RestClient) Fetch(apiName string, apiArgs []string, apiKArgs map[string]interface{}) Response {

	return Response{}
}

// Close the net.Conn
func (client *RestClient) Close() {
}

// RefreshToken will request a token by admin-token
func (client *RestClient) RefreshToken(tokenPath string) {
	//TODO: LOCK
	f, err := os.Open(tokenPath)
	if err != nil {
		return
	}
	var buf []byte
	_, err = f.Read(buf)
	atoken := string(buf)
	req, _ := http.NewRequest("POST", client.URL, nil)
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("X-Admin-Token", atoken)
	res, err := client.connect.Do(req)
	if err != nil {

	}
	defer res.Body.Close()
	client.authToken = res.Header.Get("X-Auth-Token")
}

func (client *RestClient) ReqVersion() {
	url := client.URL + "\\"
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("X-Auth-Token", client.authToken)
	res, _ := client.connect.Do(req)
	defer res.Body.Close()

}
