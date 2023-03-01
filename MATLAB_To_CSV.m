%% IF THERE ARE ANY NON-INTEGER AND/OR NON-CHAR/STRING VARIBALES LIKE
%% SIMULATION_SASESSION GO TO THE FOR LOOP WITH THE COMMENT "GET RID OF THESE VARIABLES
%% IN "variableCellArray" AND ADD THE NEW NON_INTEGER VARIABLE TO IT

% Store all variables in variables_In_Current_Workspace
variables_In_Current_Workspace = whos;

% Create all the variables needed that will be used for converting the
% variables and their values into a csv file
array_of_non_scalars_index_ = {};
array_of_matrix_names = {};
oneRowCellArray = {};
string_indicator = {};
variableCellArray = {};

% Use a loop to determine what variables in the Current Workspace are
% matrices and store them in "array_of_non_scalars" and store the matrix names in the
% "array_of_matrix_names" cell array and store the variables that contain a
% single string in the "string indicator array"
for i = 1 : length(variables_In_Current_Workspace)
       if(~isscalar(eval(variables_In_Current_Workspace(i).name)) && isnumeric(eval(variables_In_Current_Workspace(i).name)))
               array_of_non_scalars_index_{end + 1} = i;           
               array_of_matrix_names{end + 1} = variables_In_Current_Workspace(i).name;   
       elseif(~isscalar(eval(variables_In_Current_Workspace(i).name)) && isstring(eval(variables_In_Current_Workspace(i).name)))
               array_of_non_scalars_index_{end + 1} = i;
               array_of_matrix_names{end + 1} = variables_In_Current_Workspace(i).name;
               string_indicator{end + 1} = variables_In_Current_Workspace(i).name;
       elseif(~isscalar(eval(variables_In_Current_Workspace(i).name)) && ischar(eval(variables_In_Current_Workspace(i).name)) && variables_In_Current_Workspace(i).size(1,1) > 1)
               array_of_non_scalars_index_{end + 1} = i;
               array_of_matrix_names{end + 1} = variables_In_Current_Workspace(i).name;
       elseif(isstring(eval(variables_In_Current_Workspace(i).name)))
               string_indicator{end +1} = variables_In_Current_Workspace(i).name;
       end
end

% Using the "array_of_non_scalars_index", assign the reshaped matrix
% variables into the cell array "oneRowCellArray"
if(~isempty(array_of_non_scalars_index_))
   for i = 1: length(array_of_non_scalars_index_)
       oneRowCellArray{end + 1} = reshape(eval(variables_In_Current_Workspace(array_of_non_scalars_index_{i}).name)', 1, []);
   end
end

% Figure out which of the oneRow elements has the most amount of rows
if(~isempty(oneRowCellArray))
   maxColumnSize = length(oneRowCellArray{1});
   for i = 1: length(oneRowCellArray) - 1
       if(length(oneRowCellArray{i +1}) > maxColumnSize)
           maxColumnSize = length(oneRowCellArray{i + 1});
       end
   end
else
   maxColumnSize = 1;
end


% Create the column titles for the cell array, "variableCellArray"
 for i = 1: maxColumnSize + 4
   if(i == 1)
      variableCellArray{1,i} = "Variable";
   elseif(i == 2)
       variableCellArray{1,i} = "String? Y/N";
   elseif(i == 3)
       variableCellArray{1,i} = "Row";
   elseif(i == 4)
       variableCellArray{1,i} = "Column";
   else
       variableCellArray{1,i} = strcat("value", string(i - 4));
   end
 end

% Puts the variable name in the first column of "variablecellArray", 
% autimatically puts N for no string in the second column and the puts the values 
% in the rest of the columns 
if(~isempty(array_of_matrix_names))
           for i = 2 : length(variables_In_Current_Workspace) + 1
               for j = 1: maxColumnSize + 4
                if(j == 1)
                    variableCellArray{i,j} = variables_In_Current_Workspace(i - 1).name;       
                elseif(j == 2)
                    variableCellArray{i,j} = "N";
                elseif(j == 3)
                    variableCellArray{i,j} = variables_In_Current_Workspace(i - 1).size(1,1);
                elseif(j == 4)
                   variableCellArray{i,j} = variables_In_Current_Workspace(i - 1).size(1,2);
                elseif(j == 5)
                   variableCellArray{i,j} = eval(variables_In_Current_Workspace(i - 1).name);          
                else
                   variableCellArray{i,j} = [];
                end
              end
           end
  else
       for i = 2 : length(variables_In_Current_Workspace) + 1
            for j = 1: 5
                 if (j == 1)
                     variableCellArray{i,j} = variables_In_Current_Workspace(i - 1).name;             
                 elseif(j == 2)
                     variableCellArray{i,j} = "N";
                 elseif(j == 3)
                     variableCellArray{i,j} = variables_In_Current_Workspace(i - 1).size(1,1);
                 elseif(j == 4)
                     variableCellArray{i,j} = variables_In_Current_Workspace(i - 1).size(1,2);
                 else                     
                     variableCellArray{i,j} = eval(variables_In_Current_Workspace(i - 1).name);                 
                 end
             end
        end
end

% Puts a Y in the second column of variableCellArray which indicates if the 
% variable is a string or not
if(~isempty(string_indicator))
   for i = 1: length(string_indicator)
       for j = 2: size(variableCellArray,1)
           if(strcmp(variableCellArray{j,1}, string_indicator{1,i}))
               variableCellArray{j,2} = "Y";
           end           
       end
   end
end


% Puts the matrix values in "variableCellArray"
   if(~isempty(array_of_matrix_names))
     for i = 2 : size(variableCellArray,1)
      for l = 1 : length(array_of_matrix_names)
        if (strcmp(variableCellArray{i,1}, array_of_matrix_names{1,l}) == 1)
           for index = 1 : length(oneRowCellArray{1,l})
               variableCellArray{i,index + 4} = oneRowCellArray{1,l}(1,index);
           end
        end
      end
     end
   end

% Gets rid of these variables in the "variableCellArray"
for i = size(variableCellArray,1) : -1: 1
   if (strcmp(variableCellArray{i,1}, "ans"))

% Clears all of the varibles that were solely created for this program
clear ans
clear array_of_non_scalars_index_
clear index
clear i
clear j
clear l
clear maxColumnSize

% Create a csv file from variableCellArray
writecell(variableCellArray,"variable_workspace.csv")

