*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${username}              foguetesovietico
${password}              saviogatoboy22
${username_locator}      //*[@id="loginForm"]/div/div[1]/div/label/input
${password_locator}      //*[@id="loginForm"]/div/div[2]/div/label/input
${submit}                //*[@id="loginForm"]/div/div[3]/button
${profile_locator}       css=div:nth-child(8) .x1i10hfl > .x9f619
${followers_locator}     css=.xl565be:nth-child(2) > .x1i10hfl
${remove_follower}       css=.x1dm5mii:nth-child(1) .x9f619 > .x1i10hfl
${follow_button}         css=.\_acan
${follow_verify}         css=span > .x5n08af
${message_button}        css=.xjyslct
${message_box}           css=.x1gg8mnh
${message_content}       Mensagem enviada pelo Bot.
${boolean}               0
${agora_não}             css=.xjqpnuy
${recusar}               css=.\_a9_1
*** Keywords ***
Abrir Instagram
    Open Browser  https://www.instagram.com/  chrome
Colocar informações e enviar
    Wait Until Element Is Visible  ${username_locator}
    Input Text     ${username_locator}    ${username} 
    Input Text     ${password_locator}    ${password} 
    Click Element  ${submit}
Agora não
    Wait Until Element Is Visible    ${agora_não}    10s
    Click Element    ${agora_não}
    Wait Until Element Is Visible    ${recusar}    10s
    Click Element   ${recusar}
Entrar no perfil
    Wait Until Element Is Visible    ${profile_locator}    10s
    Click Element    ${profile_locator}
Entrar em seguidores
    Wait Until Element Is Visible    ${followers_locator}    10s
    Click Element    ${followers_locator}
Navegar até um perfil
    Wait Until Element Is Visible    ${remove_follower}
    Press Keys    None    TAB
    Press Keys    None    TAB
    Press Keys    None    TAB
Confirmar usuário
    Press Keys    None    ENTER
Verificar se segue e entrar em mensagens
    TRY
        Wait Until Element Is Visible   ${follow_verify}    3s
        Go Back
    EXCEPT
        ${boolean}=      Set Variable    1
        Wait Until Element Is Visible   ${follow_button}
        Click Button                    ${follow_button}
        Wait Until Element Is Visible   ${message_button}
        Click Element                   ${message_button}
        Wait Until Element Is Visible   ${message_box}    10s
        Click Element    ${message_box}
        Sleep    .2s
        Press Keys    None    ${message_content}
        Press Keys    None    ENTER
        Entrar no perfil
        Entrar em seguidores
    END
Enviar mensagem
    Wait Until Element Is Visible    ${message_box}
    Sleep    .2s
    Press Keys    None    ${message_content}
    Press Keys    None    ENTER
Keywords para loop  
    [Arguments]    ${args} 
    FOR  ${i}  IN RANGE  ${args}
        Navegar até um perfil         
    END
    Confirmar usuário
    Verificar se segue e entrar em mensagens
*** Test Cases ***
Inicar e fazer login
    Abrir Instagram
    Colocar informações e enviar
    Agora não
Ir até os seguidores
    Entrar no perfil
    Entrar em seguidores
Interações com seguidores
    ${voltas} =   Set Variable    1
    WHILE  True
        Keywords para loop    ${voltas}
        ${voltas} =  Evaluate    ${voltas} + 1
    END