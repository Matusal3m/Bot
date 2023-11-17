*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${username}              coacervados77
${password}              saviogatoboy22
${username_locator}      //*[@id="loginForm"]/div/div[1]/div/label/input
${password_locator}      //*[@id="loginForm"]/div/div[2]/div/label/input
${submit}                //*[@id="loginForm"]/div/div[3]/button
${search_locator}        css=div:nth-child(2) > .x4k7w5x .x1i10hfl > .x9f619
${search_input_locator}  //input[@value='']
${user_locate}           xpath=//div[2]/div/a/div
${user}                  isaac_salless
${follow_button}         css=.\_acan
${follow_verify}         css=span > .x5n08af
${message_button}        css=.x1lku1pv
${message_box}           css=.x1gg8mnh
${message_content}       Mensagem enviada pelo Bot.
*** Keywords ***
Abrir Instagram
    Open Browser  https://www.instagram.com/  edge
Colocar informações e enviar
    Wait Until Element Is Visible  ${username_locator}
    Input Text     ${username_locator}    ${username} 
    Input Text     ${password_locator}    ${password} 
    Click Element  ${submit}
Clicar no botão de pesquisa
    Wait Until Element Is Visible    ${search_locator}    10s
    Click Element                    ${search_locator}
CLicar na barra de pesquisa e pesquisar usuário
    Wait Until Element Is Visible    ${search_input_locator}  10s
    Input Text     ${search_input_locator}     ${user}
CLicar no usuário
    Wait Until Element Is Visible    ${user_locate}
    Click Element    ${user_locate}
Seguir usuário e mandar mensagem
    TRY
        Wait Until Element Is Visible   ${follow_verify}
    EXCEPT
        Wait Until Element Is Visible   ${follow_button}
        Click Button                    ${follow_button}
    FINALLY
        Wait Until Element Is Visible   ${message_button}
        Click Element                   ${message_button}
    END
Enviar mensagem
    Wait Until Element Is Visible    ${message_box}
    Press Keys    None    ${message_content}
    Press Keys    None    ENTER
*** Test Cases ***
Inicar e fazer login
    Abrir Instagram
    Colocar informações e enviar
Pesquisar usuário
    Clicar no botão de pesquisa
    CLicar na barra de pesquisa e pesquisar usuário
    CLicar no usuário
    Sleep    10s
Interação com o usuário
    Seguir usuário e mandar mensagem
    Enviar mensagem
    Sleep    10s
    