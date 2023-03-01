%% IF THERE IS A NON_INTEGER/NON-CHAR/NON-STRING VARIABLE LIKE SIMULATION_SASESSION, 
%% ADD IT TO THE clearvars LIST OF VARIABLES DOWN BELOW AND MAKE SURE THE CSV FILE
%% YOU USED TO ADD AND DELETE VARIABLES MATCHES THE NAME DOWN BELOW ON
%% "variableCellArray's" ASSIGNMENT STATMEENT

% Clear the workspace so that if a variable was deleted on the new csv
% file, it will show up as deleted on the workspace
clearvars -except variant_observer_aexf_mrm_18_forward variant_observer_dead_reckoning variables_In_Current_Workspace out simulation_sasession string_indicator

% Assign the variables and their values from the csv file to a cell array
variableCellArray = readcell('edited - variable_workspace.csv');

c = readcell('variable_workspace.csv');

% Get rid of the missing elements and replace them with a square brackets
for i = 1: size(variableCellArray,1)
    for j = 1 : size(variableCellArray,2)
      if ismissing(variableCellArray{i,j})
         variableCellArray{i,j} = [];
      end
    end
end


% Use a for loop to dynamically create the variables in "variableCellArray" into the
% workspace
    if(size(variableCellArray,2) ~= 5)
      for i = 2: size(variableCellArray,1)
        for j = 5 : 5
            if(~isempty(variableCellArray{i,j}) && ~isempty(variableCellArray{i,j + 1}))
                eval([variableCellArray{i,1}  '= [variableCellArray{i,j}, variableCellArray{i, j +1}]'])
            elseif(~isempty(variableCellArray{i,j}))
                eval([variableCellArray{i,1}  '= variableCellArray{i,j}'])
            end
         end
    end
  else
    for i = 2: size(variableCellArray,1)
        for j = 5 : 5
            if(~isempty(variableCellArray{i,j}))
                eval([variableCellArray{i,1}  '= variableCellArray{i,j}'])
            end
        end
    end
  end



% Update the "variables_In_Current_Workspace" with the new variables added
% on the csv file 
variables_In_Current_Workspace = whos;

% Determine which of the variables in "variableCellArray" are matrices and from there
% assign the elements to a tempary cell array called "arrayholder", and
% after "arrayholder" has all of the variables elements, use an eval
% statement to assign the actual variable the elements that "arrayholder"
% has; This code accounts for strings because when the csv file is imported
% it makes all text characters, so there is an if statment that checks if
% there is a Y next to the variables, and if there is, then arrayholder 
% adds the string values by using the convertCharsToString function and
% then later typecasts arrayholder to a string because it turns arryholder
% into a string array from a cell array, and from there, it reshapes it
    for i = 2: size(variableCellArray,1)
        arrayholder = {};
        containsString = false;
        if(~isscalar(eval(variableCellArray{i,1})))
            for j = 5 : size(variableCellArray,2) 
              if(~isempty(variableCellArray{i,j}) && strcmp(variableCellArray{i,2}, "Y")) 
                    containsString = true;
                    arrayholder{end + 1} = convertCharsToStrings(variableCellArray{i,j});
              elseif(~isempty(variableCellArray{i,j}))
                    arrayholder{end + 1} = variableCellArray{i, j};
              end
                
            end         
             if(size(arrayholder,2) >= 2)                 
                 if(containsString)
                     arrayholder = string(arrayholder);
                     arrayholder = reshape(arrayholder',variableCellArray{i,4}, variableCellArray{i,3})';  
                     eval([variableCellArray{i,1} '= convertCharsToStrings(arrayholder)'])
                 else
                    arrayholder = cell2mat(arrayholder);
                    arrayholder = reshape(arrayholder',variableCellArray{i,4}, variableCellArray{i,3})'; 
                    eval([variableCellArray{i,1} '= arrayholder']) 
                 end
            end
        end
   end
       

    % This will check to see if there are any 1x1 string variables, and convert
    % them into string variables because they will autimatically be of 
    % type character
    for i = 2: size(variableCellArray,1)
        for j = 2: 2
            if(strcmp(variableCellArray{i,j}, "Y") && variableCellArray{i,3} == 1 && variableCellArray{i,4} == 1)
                eval([variableCellArray{i,1} '= convertCharsToStrings(variableCellArray{i,5})'])
            end
        end
    end


% Clears all of the varibles that were solely created for this program
clear arrayholder
clear variableCellArray
clear i
clear index
clear j
clear variables_In_Current_Workspace
clear string_indicator
clear containsString
