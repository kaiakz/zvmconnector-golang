package zvmconnector

import "encoding/json"

// Response https://cloudlib4zvm.readthedocs.io/en/latest/restapi.html#response-data-definition
type Response struct {
	Rs        int             `json:"rs"`        // The reason code for API request.
	OverallRC int             `json:"overallRC"` // The overall return code for API request.
	ModID     int             `json:"modID"`     // The module ID that causes the error to occur.
	Rc        int             `json:"rc"`        // The return code for API request.
	Errmsg    string          `json:"errmsg"`    // The error message returned for API request. It can be empty if no error occur.
	Output    json.RawMessage `json:"output"`    // The return data from API request.
}

type Output interface{}

type Version struct {
	ApiVersion string `json:api_version`
	MinVersion string `json:min_version`
	MaxVersion string `json:max_version`
	Version    string `json:version`
}
