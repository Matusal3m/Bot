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
${follow_back_button}    css=.\_acan
${follow_back_verify}    css=span > .x5n08af
${message_button}        css=.xjyslct
${message_box}           css=.x1gg8mnh
${message_content}       Mensagem enviada pelo Bot.
${not_now}               css=.xjqpnuy
${refuse_button}         css=.\_a9_1
${follow_button}         xpath=//button[contains(.,'Seguir')]
${private_account}       css=.\_aady
${stop_follow}           css=.\_a9-_
*** Keywords ***
Abrir Instagram
    Open Browser  https://www.instagram.com/  chrome
Colocar informações e enviar
    Wait Until Element Is Visible  ${username_locator}
    Input Text     ${username_locator}    ${username} 
    Input Text     ${password_locator}    ${password} 
    Click Element  ${submit}
Agora não
    Wait Until Element Is Visible    ${not_now}    10s
    Click Element    ${not_now}
    Wait Until Element Is Visible    ${refuse_button}    10s
    Click Element   ${refuse_button}
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
    Sleep     .05s
Confirmar usuário
    Press Keys    None    ENTER
Verificar se segue e entrar em mensagens
    TRY
        Wait Until Element Is Visible      ${follow_back_verify}    3s
        Go Back
    EXCEPT
        Wait Until Element Is Visible      ${follow_back_button}
        Click Button                       ${follow_back_button}
        TRY
            Page Should Not Contain Element    ${stop_follow}
            Wait Until Element Is Visible      ${message_button}    2s
            Click Element                      ${message_button}
            Wait Until Element Is Visible      ${message_box}    
            Click Element                      ${message_box}
            Sleep    .2s
            Press Keys    None                 ${message_content}
            Press Keys    None    ENTER
            Entrar no perfil
            Entrar em seguidores
        EXCEPT
            Press Keys    None    ESC
            Go Back
        END
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