package zvmconnector

import (
	"time"
)

// Connect provide some function
type Connect interface {
	Fetch(apiName string, apiArgs []string, apiKArgs map[string]interface{}) Response
	Close()
}

// Response https://cloudlib4zvm.readthedocs.io/en/latest/restapi.html#response-data-definition
type Response struct {
	Rs        int    `json:"rs"`        // The reason code for API request.
	OverallRC int    `json:"overallRC"` // The overall return code for API request.
	ModID     int    `json:"modID"`     // The module ID that causes the error to occur.
	Rc        int    `json:"rc"`        // The return code for API request.
	Errmsg    string `json:"errmsg"`    // The error message returned for API request. It can be empty if no error occur.
	Output    string `json:"output"`    // The return data from API request.
}

// NewConnector create a RestClient or SDKSocketClient
func NewConnector(ip string, port uint16, timeout time.Duration, isRest bool) (Connect, error) {
	if isRest {
		return NewRestClient(ip, port, timeout, "")
	}
	return NewSDKSocketClient(ip, port, timeout)
}
