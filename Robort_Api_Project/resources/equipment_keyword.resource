*** Settings***

Library     RequestsLibrary
 
***Variables***

${BASE_URL}     http://127.0.0.1:5015
 
*** keywords ***

Creat API Session

    Create Session      Equipment_API       ${BASE_URL}

Get All Equipment

    [Arguments]     ${expected_status}

    ${response}=        GET On Session      Equipment_API       /api/equipment      expected_status=${expected_status} 

    RETURN      ${response}

Get Equipment by id

    [Arguments]     ${equipment_id}     ${expected_status}

    ${response}=        GET On Session      Equipment_API       /api/equipment/${equipment_id}      expected_status=${expected_status} 

    RETURN      ${response}
 