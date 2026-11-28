*** Test Cases ***
TC1_GETALL
    log To Console      Test1 Started
    ${response}=        Get All Equipment       200
    ${data}=        Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}     200
    length Should be        ${data}     3
 
TC2_GETBYID
    log To Console      Test2 Started
    ${response}=        Get Equipment by id     103     200
    ${data}=        Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}     200
    Should Be Equal As Integers     ${data}[id]     103
has context menu