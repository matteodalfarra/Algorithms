public int MyAtoi(string s) {
    s = s.Trim();
    string format_s = "";
    int i = 0;

    foreach (char c in s)
    {
        if (i == 0)
        {
            if (c != '-' && c != '+' && !int.TryParse(c.ToString(), out int n))
                break;
        }
        else
        {
            if (!int.TryParse(c.ToString(), out int n))
                break;
        }

        format_s += c.ToString();

        i++;
    }

    try
    {
        int total = int.Parse(format_s);
        return total;
    }
    catch (OverflowException e)
    {
        if (format_s.Substring(0, 1) == "-")
            return -2147483648;
        else
            return 2147483647;
    }
    catch (Exception e)
    {
        return 0;
    }
    
}